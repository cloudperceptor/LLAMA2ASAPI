########################################################
# Cloudperceptor                                        #
# #######################################################

#Use this code to test API code
import llama2
import json

response=llama2.invoke_llama2("I need a toyota camry, tell me specs for this car")

predictions = response["predictions"] 
output_text = predictions[0]
output_text = output_text.split("Output:", 1)[-1].strip()

print(output_text)

