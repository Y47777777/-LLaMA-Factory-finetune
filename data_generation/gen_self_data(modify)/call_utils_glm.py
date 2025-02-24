########################################################################################################

exec_task = {
            "name": "exec_task",
            "description": "You are an AI assistant developed by Vision Nav Corporation, and you can help users with forklift pick-up and unloading tasks through calling the [exec_task] function",
            "parameters": {
                "type": "object",
                "properties": {
                    "task_type": {
                        "type": "string",
                        "enum": ["get", "put"],
                    },
                    "location_id": {"type": "number", "description": ["The goal location represented by numbers."]},
                },
                "required": ["task_type", "location_id"],
            },
        }


exec_process = {
            "name": "exec_process",
            "description": "You are an AI assistant developed by Vision Nav Corporation, and you can call the [exec_process] function to help users execute task flow instructions",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The name of predefined process",
                    },
                    "num": {"type": "number", "description": "The number of times the task process is executed"},
                },
                "required": ["name"],
            },
        }

exec_control = {
            "name": "exec_control",
            "description": "You are an AI assistant developed by Vision Nav Corporation. You can call the [exec_control] function to help users finish AGV control commands.",
            "parameters": {
                "type": "object",
                "properties": {
                    "control_type": {
                        "type": "string",
                        "enum": ["pause", "stop", "continue", "reset", "cancel"],
                    },
                },
                "required": ["control_type"],
            },
        }

exec_query = {
            "name": "exec_query",
            "description": "You are an AI assistant developed by Vision Nav Corporation. You can call the [exec_query] function to help users complete forklift's status query instructions",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        }

exec_charge = {
            "name": "exec_charge",
            "description": "You are an AI assistant developed by Vision Nav Corporation. You can call the [exec_charge] function to help users complete AGV's charging order",
            "parameters": {
                "type": "object",
                "properties": {
                    "location_id": {"type": "number", "description": "The goal location represented by numbers."},
                },
                "required": ["location_id"],
            },
        }


tools = [
    exec_task,
    exec_process,
    exec_control,
    exec_query,
    exec_charge,
]

ack_tool_exec_charge_info = [
    {
        "name": "exec_charge",
        "arguments": {
            "location_id": "{charge_id}",
        },
    },
]

ack_tool_exec_task_info = [
    {
        "name": "exec_task",
        "arguments": {
            "task_type": "{enum_task_type}",
            "location_id": "{num_loc_id}",
        },
    },
]

ack_tool_exec_process_info = [
    {
        "name": "exec_process",
        "arguments": {
            "name": "{process_name}",
            "num": "{order_num}",
        },
    },
]

ack_tool_ctrl_info = [
    {
        "name": "exec_control",
        "arguments": {
            "control_type": "{ctrl_name}",
        },
    },
]

ack_tool_exec_query_info = [
    {
        "name": "exec_query",
        "arguments": {
        }
    },
]


exec_ok_result = {
   "order_status": "success",
}

exec_ng_result = {
    "order_status": "fail",
}
exec_result = [exec_ok_result, exec_ng_result]


ans_exec_query_info = {
    "order_status": "success",
    "state_of_charge": "{num}%",
    "state_of_car": "{car_status_info}",
    "task_of_car": "{agv_task_type}",
}
