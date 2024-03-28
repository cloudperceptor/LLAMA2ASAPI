########################################################
# Cloudperceptor                                        #
# #######################################################
# This code contains logic for serverless function which is responsible 
# to accept JSON prompt and produce text output from LLAMA2 model
# Version 1.0
# @author Team Neural Netizens
import functions_framework
from markupsafe import escape
import llama2

@functions_framework.http
def handle_post_request(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    
    
    prompt=""
    if request_json and "prompt" in request_json:
        prompt = request_json["prompt"]
    
    response=llama2.invoke_llama2(prompt)
    
    predictions = response["predictions"] 
    output_text = predictions[0]
    output_text = output_text.split("Output:", 1)[-1].strip()
    
    return output_text


