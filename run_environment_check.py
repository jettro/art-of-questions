"""
Script used to verify if the environment variables are set
"""

import os

from dotenv import load_dotenv


def verify_environment_keys() -> dict:
    """Parse known environment variables and return their availability in a dict"""
    return {
        "OPENAI_API_KEY": verify_environment_key("OPENAI_API_KEY", "OpenAI"),
        "HUGGINGFACEHUB_API_TOKEN": verify_environment_key("HUGGINGFACEHUB_API_TOKEN", "Hugging Face"),
        "WEAVIATE_API_KEY": verify_environment_key("WEAVIATE_API_KEY", "Weaviate")
    }


def verify_environment_key(key: str, remote_system: str) -> bool:
    """Verify if the provided key exists in the environment. Returns a bool indicating if the key exists"""
    try:
        found_key = os.environ[key]
    except KeyError as e:
        print(f"Please set the key {key} in the .env file if you want to work with {remote_system}")
        found_key = None

    return found_key is not None


def print_environment_check_results(results: dict) -> None:
    """Prints the results of the check for all known environment variables"""
    print("\nOverview of all found and missing environment variables:")
    for key in results.keys():
        print(f"{'found' if results[key] else 'ERROR':6s} - {key}")


if __name__ == '__main__':
    load_dotenv()
    print_environment_check_results(verify_environment_keys())
