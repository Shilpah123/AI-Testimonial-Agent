import os
import json

from github import Github



def add_testimonial(testimonial):

    token = os.environ[
        "GITHUB_TOKEN"
    ]


    github = Github(token)


    repo = github.get_repo(
        "Shilpah123/shilpah123.github.io"
    )


    file = repo.get_contents(
        "data/testimonials.json"
    )


    testimonials = json.loads(
        file.decoded_content.decode()
    )


    testimonials.append(
        testimonial
    )


    repo.update_file(

        file.path,

        "Add approved testimonial",

        json.dumps(
            testimonials,
            indent=2
        ),

        file.sha
    )