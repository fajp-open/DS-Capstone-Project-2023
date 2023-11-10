
"""
x
"""

from pydantic_settings import BaseSettings
from pydantic import Field
from openai import OpenAI


# [i]                                                                                            #
# [i] Settings                                                                                   #
# [i]                                                                                            #

class Settings(BaseSettings):
    OPENAI_API_KEY: str = Field(validation_alias="OPENAI_API_KEY")


# [i]                                                                                            #
# [i] OpenAI API                                                                                 #
# [i]                                                                                            #

class GPT_Wrapper:
    def __init__(self, OPENAI_API_KEY):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def get_completion(self, prompt, model="gpt-3.5-turbo"):
        messages = [{"role": "user", "content": prompt}]

        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0,
        )

        return completion.choices[0].message.content


# [i]                                                                                            #
# [i] Vars & Instances                                                                           #
# [i]                                                                                            #

local_settings = Settings()
