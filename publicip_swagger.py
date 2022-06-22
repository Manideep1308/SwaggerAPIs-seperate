from flask import Flask, request
from flask_cors import CORS
from flasgger import Swagger
app = Flask(__name__)
CORS(app) 
swagger = Swagger(app)
 
@app.route('/ip', methods=['POST'])

def fun():
    """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: publicipname
        in: query
        type: string
        required: true
      - name: dnslabelname
        in: query
        type: string
        required: true        
      - name: publicIPAllocationMethod
        in: query
        type: string
        required: true    
      - name: publicIPAddressVersion
        in: query
        type: string
        required: true
      - name: idleTimeoutInMinutes
        in: query
        type: string
        required: true       
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """

    dnslabelname = request.args.get('dnslabelname')
    publicipname = request.args.get('publicipname')
    publicIPAllocationMethod =request.args.get('publicIPAllocationMethod')
    publicIPAddressVersion = request.args.get('publicIPAddressVersion')
    idleTimeoutInMinutes = request.args.get('idleTimeoutInMinutes')


    data = (
'{\n'
'    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",\n'
'    "contentVersion": "1.0.0.0",\n'
'    "metadata": {\n'
'      "_generator": {\n'
'        "name": "bicep",\n'
'        "version": "0.5.6.12127",\n'
'        "templateHash": "12144059695652148753"\n'
'      }\n'
'    },\n' 
'    "parameters": {\n' 
'    "dnsLabelPrefix": {\n'
'      "type": "string",\n'
'      "defaultValue": "' + str(dnslabelname) + '",\n'
'      "metadata": {\n'
'        "description": "Unique DNS Name for the Public IP used to access the Virtual Machine."\n'
'      }\n'
'   },\n'
'    "location": {\n'
'        "type": "string",\n'
'        "defaultValue": "[resourceGroup().location]",\n'
'        "metadata": {\n'
'          "description": "Location for all resources."\n'
'        }\n'
'      }\n'
'    },\n'  
'    "variables": {\n'
'    "publicIPAddressName": "' + str(publicipname) + '"\n'

'     },\n'
'    "resources": [\n'

'            {\n'
'      "type": "Microsoft.Network/publicIPAddresses",\n'   #pubicIp
'      "apiVersion": "2016-06-01",\n'
'      "name": "[variables(''\'publicIPAddressName\''')]",\n'
'      "location": "[parameters(''\'location\''')]",\n'
'      "sku": {\n'
'        "name": "Basic"\n'
'      },\n'
'      "properties": {\n'
'        "publicIPAllocationMethod": "' + str(publicIPAllocationMethod) + '",\n'
'        "publicIPAddressVersion": "' + str(publicIPAddressVersion) + '",\n'
'        "dnsSettings": {\n'
'          "domainNameLabel": "[parameters(''\'dnsLabelPrefix\''')]"\n'
'        },\n'
'        "idleTimeoutInMinutes":' +str(idleTimeoutInMinutes) + '\n'
'      }\n'
'    }\n' 
'   ]\n'
'  }\n'    

    )


    with open('publicip_template.json','w') as f:
      print(data, file=f)


    return data


app.run(port=5003, host='0.0.0.0',debug=True)   