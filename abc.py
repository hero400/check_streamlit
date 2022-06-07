import numpy as np
from flask import Flask, request, make_response
import json
import pickle
from flask_cors import cross_origin
import logging
import streamlit as st
logging.basicConfig(level=logging.INFO)
# z=True
# def webhook():
#     req = request.get_json(silent=True, force=True)
#     #print("Request:")
#     #print(json.dumps(req, indent=4))
#     res= processRequest(req)
#     res = json.dumps(res, indent=4)
#     #print(res)
#     r = make_response(res)
#     r.headers['Content-Type'] = 'application/json'
#     return r
# # def load_image():
# #     uploaded_file = st.file_uploader(label='Pick an image to test')
# #     if uploaded_file is not None:
# #         image_data = uploaded_file.getvalue()
# #         st.image(image_data)
# def hello():
#     global z
#     if z:
#         z=False
#         print("ok")
#         st.title(z)
#     else:
#         z=True
#         return st.title(z)
# def processRequest(req):
#     global top_company_changed
#     global top_companies
#     global z
#     #sessionID=req.get('responseId')
#     result = req.get("queryResult")
#     #user_says=result.get("queryText")
#     #log.write_log(sessionID, "User Says: "+user_says)
#     parameters = result.get("parameters")
#     Petal_length=parameters.get("number")
#     Petal_width = parameters.get("number1")
#     Sepal_length=parameters.get("number2")
#     Sepal_width=parameters.get("number3")
#     int_features = [Petal_length,Petal_width,Sepal_length,Sepal_width]
    
#     final_features = [np.array(int_features)]
     
#     intent = result.get("intent").get('displayName')
    
#     if (intent=='IrisData'):
#         prediction = model.predict(final_features)
    
#         output = round(prediction[0], 2)
    
        
#         if(output==0):
#             flowr = 'Setosa'
    
#         if(output==1):
#             flowr = 'Versicolour'
        
#         if(output==2):
#             flowr = 'Virginica'
       
#         fulfillmentText= "The Iris type seems to be..  {} !".format(flowr)
#         #log.write_log(sessionID, "Bot Says: "+fulfillmentText)
#         return {
#             "fulfillmentText": fulfillmentText
#         }
#     elif (intent=="SeeOurTopCompanyList"):
#         if top_company_changed:
#             return {
#             "fulfillmentText":"{}+{}".format(top_companies,z),
#              "fulfillmentMessages": [
#       {
#         "platform": "ACTIONS_ON_GOOGLE",
#         "simpleResponses": {
#           "simpleResponses": [
#             {
#               "textToSpeech":"{}+{}".format(top_companies,z)
#             }
#           ]
#         }
#       },
#       {
#       "platform": "ACTIONS_ON_GOOGLE",
#         "suggestions": {
#           "suggestions": [
#             {
#               "title": "ok"
#             }
#           ]
#         }
#       },
#       {
#         "text": {
#           "text": [
#           "{}+{}".format(top_companies,z)
            
#             ]
#         }
#       }
#     ]}
#         else:
#             return {
#             "fulfillmentText":"{}+{}".format(companies,z),
#              "fulfillmentMessages": [
#       {
#         "platform": "ACTIONS_ON_GOOGLE",
#         "simpleResponses": {
#           "simpleResponses": [
#             {
#               "textToSpeech":"{}+{}".format(companies,z)
#             }
#           ]
#         }
#       },
#       {
#       "platform": "ACTIONS_ON_GOOGLE",
#         "suggestions": {
#           "suggestions": [
#             {
#               "title": "ok"
#             }
#           ]
#         }
#       },
#       {
#         "text": {
#           "text": [
#           "{}+{}".format(companies,z)
            
#             ]
#         }
#       }
#     ]}
#     elif(intent=="NoNeedOfTopCompanies"):
#         top_company_changed=True
#         top_companies={}
#         z=False
#     elif(intent=="TimeToLeave"):
#         z=True
#         top_company_changed=False   
#         return 
#         {
#         "fulfillmentText":"bye"
#         } 
#     else:
#          return {
#             "fulfillmentText":"nope something is wrong  {}".format(intent)
#         }
#         #log.write_log(sessionID, "Bot Says: " + result.fulfillmentText)                
# def main():
#     st.title('Image upload demo')
#     app = Flask(__name__)
#     #load_image()
#     #@app.route('/')
#     hello()
#     #@app.route('/webhook', methods=['POST'])                                                #GET
#     #@cross_origin()
#     #webhook()
#     #processRequest()
    
#     #model = pickle.load(open('rf.pkl', 'rb'))
# if __name__ == '__main__':
#     main()
import streamlit as st

if not hasattr(st, 'already_started_server'):
    # Hack the fact that Python modules (like st) only load once to
    # keep track of whether this file already ran.
    st.already_started_server = True

    st.write('''
        The first time this script executes it will run forever because it's
        running a Flask server.

        Just close this browser tab and open a new one to see your Streamlit
        app.
    ''')

    from flask import Flask

    app = Flask(__name__)

    @app.route('/foo')
    def serve_foo():
        return 'This page is served via Flask!'
    @app.route('/webhook', methods=['POST'])                                                #GET
    @cross_origin()
    def webhook():
        req = request.get_json(silent=True, force=True)
        #print("Request:")
        #print(json.dumps(req, indent=4))
        res= processRequest(req)
        res = json.dumps(res, indent=4)
        #print(res)
        r = make_response(res)
        r.headers['Content-Type'] = 'application/json'
        return r


    # processing the request from dialogflow
    def processRequest(req):
        global top_company_changed
        global top_companies
        global z
        #sessionID=req.get('responseId')
        result = req.get("queryResult")
        #user_says=result.get("queryText")
        #log.write_log(sessionID, "User Says: "+user_says)
        parameters = result.get("parameters")
        Petal_length=parameters.get("number")
        Petal_width = parameters.get("number1")
        Sepal_length=parameters.get("number2")
        Sepal_width=parameters.get("number3")
        int_features = [Petal_length,Petal_width,Sepal_length,Sepal_width]
        
        final_features = [np.array(int_features)]
         
        intent = result.get("intent").get('displayName')
        
        if (intent=='IrisData'):
            prediction = model.predict(final_features)
        
            output = round(prediction[0], 2)
        
            
            if(output==0):
                flowr = 'Setosa'
        
            if(output==1):
                flowr = 'Versicolour'
            
            if(output==2):
                flowr = 'Virginica'
           
            fulfillmentText= "The Iris type seems to be..  {} !".format(flowr)
            #log.write_log(sessionID, "Bot Says: "+fulfillmentText)
            return {
                "fulfillmentText": fulfillmentText
            }
        elif (intent=="SeeOurTopCompanyList"):
            if top_company_changed:
                return {
                "fulfillmentText":"{}+{}".format(top_companies,z),
                 "fulfillmentMessages": [
          {
            "platform": "ACTIONS_ON_GOOGLE",
            "simpleResponses": {
              "simpleResponses": [
                {
                  "textToSpeech":"{}+{}".format(top_companies,z)
                }
              ]
            }
          },
          {
          "platform": "ACTIONS_ON_GOOGLE",
            "suggestions": {
              "suggestions": [
                {
                  "title": "ok"
                }
              ]
            }
          },
          {
            "text": {
              "text": [
              "{}+{}".format(top_companies,z)
                
                ]
            }
          }
        ]}
            else:
                return {
                "fulfillmentText":"{}+{}".format(companies,z),
                 "fulfillmentMessages": [
          {
            "platform": "ACTIONS_ON_GOOGLE",
            "simpleResponses": {
              "simpleResponses": [
                {
                  "textToSpeech":"{}+{}".format(companies,z)
                }
              ]
            }
          },
          {
          "platform": "ACTIONS_ON_GOOGLE",
            "suggestions": {
              "suggestions": [
                {
                  "title": "ok"
                }
              ]
            }
          },
          {
            "text": {
              "text": [
              "{}+{}".format(companies,z)
                
                ]
            }
          }
        ]}
        elif(intent=="NoNeedOfTopCompanies"):
            top_company_changed=True
            top_companies={}
            z=False
        elif(intent=="TimeToLeave"):
            z=True
            top_company_changed=False   
            return 
            {
            "fulfillmentText":"bye"
            } 
        else:
             return {
                "fulfillmentText":"nope something is wrong  {}".format(intent)
            }    
        app.run(port=8888)


# We'll never reach this part of the code the first time this file executes!

# Your normal Streamlit app goes here:
x = st.slider('Pick a number')
st.write('You picked:', x)