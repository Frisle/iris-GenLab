import bo, bp , bs, adapter

CLASSES = {
    "Python.FileOperation": bo.FileOperation,   
    "Python.NERService": bs.NERService,
    "Python.FilterPostRoutingRule": bp.FilterPostRoutingRule
}

import os

PRODUCTIONS = [{
    "PEX.Production": {
        "@Name": "PEX.Production",
        "@TestingEnabled": "true",
        "@LogGeneralTraceEvents": "false",
        "Description": "",
        "ActorPoolSize": "2",
        "Item": [
            {
                "@Name": "Python.FileOperation",
                "@Category": "",
                "@ClassName": "Python.FileOperation",
                "@PoolSize": os.environ.get('POOL_SIZE', '1'),
                "@Enabled": "true",
                "@Foreground": "false",
                "@Comment": "",
                "@LogTraceEvents": "true",
                "@Schedule": "",
                "Setting": [
                    {
                        "@Target": "Adapter",
                        "@Name": "Charset",
                        "#text": "utf-8"
                    },
                    {
                        "@Target": "Adapter",
                        "@Name": "FilePath",
                        "#text": "/home/irisowner/dev/output/"
                    },
                    {
                        "@Target": "Host",
                        "@Name": "%settings",
                        "#text": "path=/tmp/"
                    }
                ]
            },
            {
                "@Name": "Python.NERService",
                "@Category": "",
                "@ClassName": "Python.NERService",
                "@PoolSize": "1",
                "@Enabled": "true",
                "@Foreground": "false",
                "@Comment": "",
                "@LogTraceEvents": "false",
                "@Schedule": "",
                "Setting": {
                    "@Target": "Host",
                    "@Name": "%settings",
                    "#text": "limit=10"
                }
            },         
            {
                "@Name": "Python.FilterPostRoutingRule",
                "@Category": "",
                "@ClassName": "Python.FilterPostRoutingRule",
                "@PoolSize": "1",
                "@Enabled": "true",
                "@Foreground": "false",
                "@Comment": "",
                "@LogTraceEvents": "false",
                "@Schedule": ""
            }
        ]
    }
}]