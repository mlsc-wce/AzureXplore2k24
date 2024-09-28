import logging
import azure.functions as func

app = func.FunctionApp()
#Decorators
@app.blob_trigger(arg_name="myblob", path="input-texts/{name}",
                  connection="AzureWebJobsStorage") 
@app.blob_output(arg_name="outputBlob", path="processed-texts/{name}",
                 connection="AzureWebJobsStorage")
def ProcessTextFunction(myblob: func.InputStream, outputBlob: func.Out[str]):
    logging.info(f"Blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    # Read the blob content (text file)
    text = myblob.read().decode('utf-8')

    # Process the text (convert to uppercase)
    processed_text = text.upper()

    # Write the processed text to the output blob
    outputBlob.set(processed_text)
    logging.info("Text processed and saved successfully.")
