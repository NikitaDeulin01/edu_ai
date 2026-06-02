import httpx

from config import get_settings

settings = get_settings()


class LLMNotConfiguredError(Exception):
    pass


class LLMRequestError(Exception):
    pass


def ensure_llm_configured() -> None:
    if not settings.llm_enabled:
        raise LLMNotConfiguredError(
            "LLM не настроена. Добавьте LLM_API_KEY, LLM_BASE_URL и LLM_MODEL в project/.env"
        )


async def chat(
    *,
    system: str,
    user: str,
    temperature: float = 0.5,
    max_tokens: int = 2000,
) -> str:
    ensure_llm_configured()
    payload = {
        "model": settings.llm_model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    headers = {
        "Authorization": f"Bearer {settings.llm_api_key}",
        "Content-Type": "application/json",
    }
    url = f"{settings.llm_base_url}/chat/completions"
    async with httpx.AsyncClient(timeout=90.0) as client:
        response = await client.post(url, headers=headers, json=payload)
    if response.status_code >= 400:
        raise LLMRequestError(f"LLM API error {response.status_code}: {response.text[:500]}")
    data = response.json()
    try:
        return data["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError, TypeError) as exc:
        raise LLMRequestError(f"Unexpected LLM response: {data}") from exc
