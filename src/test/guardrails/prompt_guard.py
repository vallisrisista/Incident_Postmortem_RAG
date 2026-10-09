from transformers import pipeline

MODEL_ID = "meta-llama/Llama-Prompt-Guard-2-22M"

classifier = pipeline(
    "text-classification",
    model=MODEL_ID
)


def check_prompt(text: str) -> dict:
    """
    Check whether the user input looks like a jailbreak/prompt-injection attack.
    """

    result = classifier(
        text,
        truncation=True,
        max_length=512
    )[0]

    return {
        "label": result["label"],
        "score": float(result["score"]),
        "blocked": result["label"].upper() == "MALICIOUS"
    }