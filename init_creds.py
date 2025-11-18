from dopplersdk import DopplerSDK
import os

# set Doppler token
doppler_token = os.getenv("DOPPLER_AIGUILD_TOKEN")
doppler_client = DopplerSDK()
doppler_client.set_access_token(doppler_token)


def get_api_key():

    results = doppler_client.secrets.get(
        project='dep-training',
        config='prod_ai_guild_genai_practicum',
        name="AZURE_OPENAI_API_KEY"
    )
    api_key = results.value['raw']
    return api_key

def get_endpoint():

    results = doppler_client.secrets.get(
        project='dep-training',
        config='prod_ai_guild_genai_practicum',
        name="AZURE_OPENAI_API_BASE"
    )
    endpoint = results.value['raw']
    return endpoint



def main():
    api_key = get_api_key()
    endpoint = get_endpoint()

    # set the OpenAI API key for the user in environment variable
    with open(os.path.expanduser("~/.bashrc"), "a") as outfile:
        # 'a' stands for "append"  
        outfile.writelines("export AZURE_OPENAI_API_KEY="+api_key + "\n")


    # set the OpenAI API key for the user in environment variable
    with open(os.path.expanduser("~/.bashrc"), "a") as outfile:
        # 'a' stands for "append"  
        outfile.writelines("export AZURE_OPENAI_API_BASE="+endpoint + "\n")


if __name__ == "__main__":
    main()
