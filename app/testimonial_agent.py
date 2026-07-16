from datetime import datetime

from validator_agent import validate_testimonial


def process_testimonial(data):

    validation = validate_testimonial(
        data["testimonial"]
    )

    categories = categorize_testimonial(
        data["testimonial"]
    )


    result = {

        "name": data["name"],

        "role": data["role"],

        "company": data.get(
            "company",
            ""
        ),

        "linkedin": data.get(
            "linkedin",
            ""
        ),

        # Keep original words
        "testimonial": data["testimonial"],

        "date": str(
            datetime.now().date()
        ),

        "categories": categories,

        "approved": False,

        "validation": validation
    }


    return result



def categorize_testimonial(text):

    categories = []

    keywords = text.lower()


    if "ai" in keywords:
        categories.append("AI")

    if "automation" in keywords:
        categories.append("Automation")

    if (
        "team" in keywords
        or "collaboration" in keywords
    ):
        categories.append(
            "Collaboration"
        )


    return categories