from chat_template_utils import *
from call_utils_glm import *

import random
import copy
import json
import re
import random
import inflect
# from call_utils import tools

common_chat_template = {
    "conversations": [
      {
        "from": "human",
        "value": "{user_chat_info}"
      },
      {
        "from": "gpt",
        "value": "{sys_answer_info}"
      }
    ],
    "tools": "[]",

}

lang_set = ["en", "zh"]

func_call_template = {
    "conversations": [
        {
            "from": "human",
            "value": "{user_chat_info}"
        },
        {
            "from": "function_call",
            "value": "{tools_call_info}"
        },
        {
            "from": "observation",
            "value": "{tool_call_response}"
        },
        {
            "from": "gpt",
            "value": "{summary_response}"
        },
    ],
    "tools": "[{defined_function_call}]",
}


def gen_num_id(lang="en"):
    prob = random.random()
    number = random.randint(1, 10)
    chinese_numerals = {
         1: '一', 2: '二', 3: '三', 4: '四', 5: '五',
         6: '六', 7: '七', 8: '八', 9: '九', 10: '十'
    }
    if prob > 0.5:
        ordinal = number
    else:
        p = inflect.engine()
        if lang == "en":
            ordinal = p.number_to_words(number)
        else:
            ordinal = chinese_numerals[number]

    return number, ordinal


def gen_repeat_num(lang="en"):
    num = random.randint(1, 100)
    if num == 1:
        number = random.choice(["1", "one", "once"]) if lang =="en" else random.choice(["1", "一"])
    elif num == 2:
        number = random.choice(["2", "two", "twice"]) if lang == "en" else random.choice(["2", "二"])
    elif num == 3:
        number = random.choice(["3", "three", "thrice"]) if lang == "en" else random.choice(["3", "三"])
    else:
        if random.random() > 0.5 or lang == "zh":
            number = num
        else:
            p = inflect.engine()
            number = p.number_to_words(num)
    return num, number


def create_exec_charge_data(lang_info):
    # lang_info = random.choice(lang_set)
    chat_info = copy.deepcopy(func_call_template)
    # sys_template = str(copy.deepcopy(chat_info["messages"][0]["content"])).replace("{defined_function_call}",
    #                                                                                str(exec_charge))
    user_in = random.choice(charge_info) if lang_info == "zh" else random.choice(charge_info_en)

    # charge_id = random.randint(1, 10)
    number, charge_id = gen_num_id(lang_info)
    charge_id_info = str(charge_id) + "号库位" if lang_info == "zh" else str(charge_id) + " location"
    ask_charge_call = copy.deepcopy(ack_tool_exec_charge_info)
    ans_charge_call = random.choice(exec_result)

    summery_out = random.choice(ok_summary_task_info) if "success" in str(ans_charge_call) else random.choice(ng_summary_task_info)
    if lang_info == "en":
        summery_out = random.choice(ok_summary_task_info_en) if "success" in str(ans_charge_call) else random.choice(ng_summary_task_info_en)

    chat_info["tools"] = "["+str(exec_charge)+"]"
    if "charge_pos_id" not in user_in:
        ask_charge_id = random.choice(ask_charge_id_info) if "zh" in lang_info else random.choice(ask_charge_id_info_en)
        ans_charge_id = random.choice(ans_charge_id_info).replace("{charge_pos_id}", charge_id_info) if "zh" in lang_info else random.choice(ans_charge_id_info_en).replace("{charge_pos_id}", charge_id_info)

        sys_ask_dict = {"from": "gpt", "value": ask_charge_id}
        usr_ext_rsp_dict = {"from": "human", "value": ans_charge_id}

        chat_info["conversations"][0]["value"] = user_in
        chat_info["conversations"].insert(1, sys_ask_dict)
        chat_info["conversations"].insert(2, usr_ext_rsp_dict)

        ask_charge_call[0]["arguments"]["location_id"] = charge_id
        chat_info["conversations"][3]["value"] = str(ask_charge_call).replace("'", '"')
        chat_info["conversations"][4]["value"] = str(ans_charge_call).replace("'", '"')

        chat_info["conversations"][5]["value"] = summery_out
        # chat_list.append(chat_info)
    else:
        ask_charge_call[0]["arguments"]["location_id"] = charge_id

        chat_info["conversations"][0]["value"] = user_in.replace("{charge_pos_id}", charge_id_info)
        chat_info["conversations"][1]["value"] = str(ask_charge_call).replace("'", '"')
        chat_info["conversations"][2]["value"] = str(ans_charge_call).replace("'", '"')
        chat_info["conversations"][3]["value"] = summery_out
    return chat_info, charge_id


def create_get_goods_data(lang_info, weights=[0.5, 0.5]):
    # lang_info = random.choice(lang_set)
    chat_info = copy.deepcopy(func_call_template)
    user_in = random.choice(get_goods_info) if lang_info == "zh" else random.choice(get_goods_info_en)

    # get_id = random.randint(1, 10)
    number, get_id = gen_num_id(lang_info)
    get_id_info = str(get_id) + "号库位" if lang_info == "zh" else "location " + str(get_id)
    user_in = user_in.replace("{transport_plan_id}", "默认")
    user_input = user_in
    task_type = "get"
    ack_tool_exec_task_info[0].get('arguments')["location_id"] = number
    ack_tool_call_info = str(ack_tool_exec_task_info).replace("'", '"').replace("{enum_task_type}", task_type).replace("'", '"')
    # ack_tool_call_info = str(ack_tool_exec_task_info).replace("'", '"').replace("{enum_task_type}", task_type).replace(
    #     "{num_loc_id}", str(number)).replace("'", '"')

    ans_tool_call_info = str(random.choices(exec_result, weights=weights, k=1)[0]).replace("'", '"')
    summery_out = random.choice(ok_summary_task_info) if "success" in ans_tool_call_info else random.choice(
        ng_summary_task_info)
    if lang_info == "en":
        summery_out = random.choice(ok_summary_task_info_en) if "success" in ans_tool_call_info else random.choice(
        ng_summary_task_info_en)

    chat_info["tools"] = "["+str(exec_task)+"]"
    info = ""
    if 'get_pos_id' not in user_input:
        ask_get_pos_id_info = random.choice(ask_get_goods_pos_id_info) if "zh" in lang_info else random.choice(ask_get_goods_pos_id_info_en)

        ans_get_pos_id_info = (random.choice(ans_get_goods_pos_id_info)).replace("{get_pos_id}", get_id_info) if "zh" in lang_info else (random.choice(ans_get_goods_pos_id_info_en)).replace("{get_pos_id}", get_id_info)

        sys_ask_dict = {"from": "gpt", "value": ask_get_pos_id_info}
        usr_ext_rsp_dict = {"from": "human", "value": ans_get_pos_id_info}
        # sys_ask_dict = {"role": "assistant", "content": ask_get_pos_id_info}
        # usr_ext_rsp_dict = {"role": "user", "content": ans_get_pos_id_info}

        chat_info["conversations"][0]["value"] = user_input
        chat_info["conversations"].insert(1, sys_ask_dict)
        chat_info["conversations"].insert(2, usr_ext_rsp_dict)

        # ack_tool_call_info[0]["parameters"]["location_id"] = charge_id
        chat_info["conversations"][3]["value"] = ack_tool_call_info
        chat_info["conversations"][4]["value"] = ans_tool_call_info

        chat_info["conversations"][5]["value"] = summery_out

    else:
        user_input = user_input.replace("{get_pos_id}", get_id_info)

        chat_info["conversations"][0]["value"] = user_input
        chat_info["conversations"][1]["value"] = ack_tool_call_info
        chat_info["conversations"][2]["value"] = ans_tool_call_info
        chat_info["conversations"][3]["value"] = summery_out

    return chat_info, number


def create_agv_operate_query_data(lang_info):
    chat_info = copy.deepcopy(func_call_template)

    user_in = random.choice(ask_agv_operate_status)
    res_out = random.choice(ans_agv_operate_status)
    oder_out = random.choice(car_status_info) if lang_info == "zh" else random.choice(car_status_info_en)
    agv_task_out = random.choice(task_status_info) if lang_info == "zh" else random.choice(task_status_info_en)
    ele_val = random.randint(0, 100)
    res_out = res_out.replace("{num}", str(ele_val)).replace("{car_status_info}", str(oder_out)).replace("{agv_task_type}", str(agv_task_out))
    ans_query_info = str(ans_exec_query_info).replace("{num}", str(ele_val)).replace("{car_status_info}", str(oder_out)).replace("{agv_task_type}", str(agv_task_out))
    ans_query_info = ans_query_info.replace("'", '"')

    ack_query_info = str(ack_tool_exec_query_info).replace("'", '"')

    chat_info["tools"] = "["+str(exec_query)+"]"
    chat_info["conversations"][0]["value"] = user_in
    chat_info["conversations"][1]["value"] = ack_query_info
    chat_info["conversations"][2]["value"] = ans_query_info
    chat_info["conversations"][3]["value"] = res_out

    return chat_info

# def create_agv_task_query_data(lang_info):
#     chat_info = copy.deepcopy(func_call_template)
#     # chat_str = str(copy.deepcopy(query_call_template))
#     user_in = random.choice(ask_agv_task_query)
#
#     res_out = random.choice(ans_agv_task_query)
#     oder_out = random.choice(task_status_info_en)
#     ele_val = random.randint(0, 100)
#     res_out = res_out.replace("{agv_task_type}", str(oder_out))
#     ans_query_info = str(ans_exec_query_info).replace("{num}", str(ele_val)).replace("{agv_task_type}", str(oder_out)).replace("{car_status_info}", "")
#     ans_query_info = ans_query_info.replace("'", '"')
#
#     ack_query_info = str(ack_tool_exec_query_info).replace("'", '"')
#
#     chat_info["tools"] = "["+str(exec_query)+"]"
#     chat_info["conversations"][0]["value"] = user_in
#     chat_info["conversations"][1]["value"] = ack_query_info
#     chat_info["conversations"][2]["value"] = ans_query_info
#     chat_info["conversations"][3]["value"] = res_out
#
#     return chat_info

def create_status_query_data(lang_info):
    chat_info = copy.deepcopy(func_call_template)
    # chat_str = str(copy.deepcopy(query_call_template))
    user_in = random.choice(car_query_info) if lang_info == "zh" else random.choice(car_query_info_en)

    res_out = random.choice(ok_ans_car_query_info) if lang_info == "zh" else random.choice(ok_ans_car_query_info_en)
    oder_out = random.choice(car_status_info) if lang_info == "zh" else random.choice(car_status_info_en)
    agv_task_out = random.choice(task_status_info) if lang_info == "zh" else random.choice(task_status_info_en)
    ele_val = random.randint(0, 100)
    res_out = res_out.replace("{num}", str(ele_val)).replace("{car_status_info}", str(oder_out)).replace("{agv_task_type}", str(agv_task_out))
    ans_query_info = str(ans_exec_query_info).replace("{num}", str(ele_val)).replace("{car_status_info}", str(oder_out)).replace("{agv_task_type}", str(agv_task_out))
    ans_query_info = ans_query_info.replace("'", '"')

    ack_query_info = str(ack_tool_exec_query_info).replace("'", '"')

    chat_info["tools"] = "["+str(exec_query)+"]"
    chat_info["conversations"][0]["value"] = user_in
    chat_info["conversations"][1]["value"] = ack_query_info
    chat_info["conversations"][2]["value"] = ans_query_info
    chat_info["conversations"][3]["value"] = res_out

    return chat_info

def create_self_query_data(lang_info):
    chat_info = copy.deepcopy(common_chat_template)
    user_in = random.choice(self_query_info_en) if lang_info == "en" else random.choice(self_query_info_zh)

    sys_out = random.choice(ans_self_query_info_en) if lang_info == "en" else random.choice(ans_self_query_info_zh)
    chat_info["conversations"][0]["value"] = user_in
    chat_info["conversations"][1]["value"] = sys_out
    return chat_info

def create_purpose_query_data(lang_info):
    chat_info = copy.deepcopy(common_chat_template)
    user_in = random.choice(ask_purpose_query_info_en)

    sys_out = random.choice(ans_purpose_query_info_en)
    chat_info["conversations"][0]["value"] = user_in
    chat_info["conversations"][1]["value"] = sys_out
    return chat_info


def create_agv_loc_query_data(lang_info):
    chat_info = copy.deepcopy(common_chat_template)
    user_in = random.choice(ask_agv_loc_query)

    sys_out = random.choice(ans_agv_loc_query)
    chat_info["conversations"][0]["value"] = user_in
    chat_info["conversations"][1]["value"] = sys_out
    return chat_info

def create_common_query_data(lang_info):
    chat_info = copy.deepcopy(common_chat_template)
    user_in = random.choice(do_query_info) if lang_info == "zh" else random.choice(do_query_info_en)

    sys_out = random.choice(ans_do_query_info) if lang_info == "zh" else random.choice(ans_do_query_info_en)
    chat_info["conversations"][0]["value"] = user_in
    chat_info["conversations"][1]["value"] = sys_out

    return chat_info

def create_put_goods_data(lang_info, weights=[0.5, 0.5]):
    # lang_info = random.choice(lang_set)
    chat_info = copy.deepcopy(func_call_template)
    user_in = random.choice(put_goods_info) if "zh" == lang_info else random.choice(put_goods_info_en)
    # put_id = random.randint(1, 10)
    number, put_id = gen_num_id(lang_info)
    put_id_info = str(put_id) + "号库位" if "zh" == lang_info else "location " + str(put_id)
    user_in = user_in.replace("{transport_plan_id}", "默认")
    user_input = user_in
    task_type = "put"
    ack_tool_exec_task_info[0].get('arguments')["location_id"] = number
    ack_tool_call_info = str(ack_tool_exec_task_info).replace("'", '"').replace("{enum_task_type}", task_type).replace("'", '"')
    # ack_tool_call_info = str(ack_tool_exec_task_info).replace("'", '"').replace("{enum_task_type}", task_type).replace(
    #     "{num_loc_id}", str(number)).replace("'", '"')

    ans_tool_call_info = str(random.choices(exec_result, weights=weights, k=1)[0]).replace("'", '"')
    summery_out = random.choice(ok_summary_task_info) if "success" in ans_tool_call_info else random.choice(
        ng_summary_task_info)
    if "en" == lang_info:
        summery_out = random.choice(ok_summary_task_info_en) if "success" in ans_tool_call_info else random.choice(
            ng_summary_task_info_en)

    chat_info["tools"] = "["+str(exec_task)+"]"
    info = ""
    if 'put_goods_id' not in user_input:
        ask_put_goods_id = random.choice(ask_put_goods_id_info) if "zh" == lang_info else random.choice(ask_put_goods_id_info_en)
        ans_put_goods_id = str(random.choice(ans_put_goods_id_info)).replace("{put_goods_id}", put_id_info) if "zh"==lang_info else str(random.choice(ans_put_goods_id_info_en)).replace("{put_goods_id}", put_id_info)
        # ans_put_goods_id = ans_put_goods_id.replace("{put_goods_info}", put_id_info)

        sys_ask_dict = {"from": "gpt", "value": ask_put_goods_id}
        usr_ext_rsp_dict = {"from": "human", "value": ans_put_goods_id}
        # sys_ask_dict = {"role": "assistant", "content": ask_put_goods_id}
        # usr_ext_rsp_dict = {"role": "user", "content": ans_put_goods_id}

        chat_info["conversations"][0]["value"] = user_input
        chat_info["conversations"].insert(1, sys_ask_dict)
        chat_info["conversations"].insert(2, usr_ext_rsp_dict)

        # ack_tool_call_info[0]["parameters"]["location_id"] = charge_id
        chat_info["conversations"][3]["value"] = ack_tool_call_info
        chat_info["conversations"][4]["value"] = ans_tool_call_info

        chat_info["conversations"][5]["value"] = summery_out

    else:
        user_input = user_input.replace("{put_goods_id}", put_id_info)

        chat_info["conversations"][0]["value"] = user_input
        chat_info["conversations"][1]["value"] = ack_tool_call_info
        chat_info["conversations"][2]["value"] = ans_tool_call_info
        chat_info["conversations"][3]["value"] = summery_out

    return chat_info, number


def create_get_put_data(lang_info, weights=[0.5, 0.5]):
    # lang_info = random.choice(lang_set)
    chat_info = copy.deepcopy(func_call_template)
    user_in = random.choice(get_put_info) if "zh" == lang_info else random.choice(get_put_info_en)
    get_number, get_id = gen_num_id(lang_info)
    put_number, put_id = gen_num_id(lang_info)
    # get_id = random.randint(1, 10)
    # put_id = random.randint(1, 10)
    while get_number == put_number:
        put_number, put_id = gen_num_id(lang_info)
        # put_id = random.randint(1, 10)

    get_id_info = str(get_id) + "号库位" if "zh" == lang_info else "location " + str(get_id)
    put_id_info = str(put_id) + "号库位" if "zh" == lang_info else "location " + str(put_id)

    ack_get_task_call_info = copy.deepcopy(ack_tool_exec_task_info)
    ack_get_task_call_info[0]["arguments"]["task_type"] = "get"
    ack_get_task_call_info[0]["arguments"]["location_id"] = get_number
    ask_get_task_call_info = str(ack_get_task_call_info).replace("'", '"')

    ack_put_task_call_info = copy.deepcopy(ack_tool_exec_task_info)
    ack_put_task_call_info[0]["arguments"]["task_type"] = "put"
    ack_put_task_call_info[0]["arguments"]["location_id"] = put_number
    ask_put_task_call_info = str(ack_put_task_call_info).replace("'", '"')

    # ans_get_task_call_info = random.choice(exec_result)
    ans_get_task_call_info = random.choices(exec_result, weights=weights, k=1)[0]
    ans_get_task_call_str = str(ans_get_task_call_info).replace("'", '"')

    # ans_put_task_call_info = random.choice(exec_result)
    ans_put_task_call_info = random.choices(exec_result, weights=weights, k=1)[0]
    ans_put_task_call_str = str(ans_put_task_call_info).replace("'", '"')

    get_summary_info = random.choice(ok_summary_task_info) if "success" in ans_get_task_call_str else random.choice(ng_summary_task_info)
    if "en" == lang_info:
        get_summary_info = random.choice(ok_summary_task_info_en) if "success" in ans_get_task_call_str else random.choice(
            ng_summary_task_info_en)
    put_summary_info = random.choice(ok_summary_task_info) if "success" in ans_put_task_call_str else random.choice(ng_summary_task_info)
    if "en" == lang_info:
        put_summary_info = random.choice(ok_summary_task_info_en) if "success" in ans_put_task_call_str else random.choice(ng_summary_task_info_en)

    chat_info["tools"] = "[" + str(exec_task) + "]"
    chat_info["conversations"][0]["value"] = user_in.replace("{get_pos_id}", get_id_info).replace("{put_goods_id}",
                                                                                                  put_id_info).replace(
        "{transport_plan_id}", "默认")


    chat_info["conversations"][1]["value"] = ask_get_task_call_info
    chat_info["conversations"][2]["value"] = ans_get_task_call_str

    if "fail" in ans_get_task_call_str:
        chat_info["conversations"][3]["value"] = random.choice(ng_get_summary_task_info) if "zh"==lang_info else random.choice(ng_get_summary_task_info_en)
        return chat_info, get_number, put_number

    ask_put_tool_dict = {"from": "function_call", "value": ask_put_task_call_info}
    ans_put_tool_dict = {"from": "observation", "value": ans_put_task_call_str}
    summary_dict = {"from": "gpt", "value": put_summary_info}
    chat_info["conversations"][3] = ask_put_tool_dict
    chat_info["conversations"].insert(4, ans_put_tool_dict)
    chat_info["conversations"].insert(5, summary_dict)

    return chat_info, get_number, put_number


def create_task_process_data(lang_info, weights=[0.5, 0.5]):
    # lang_info = random.choice(lang_set)
    # num = random.randint(1, 100)
    number, repeat_id = gen_repeat_num(lang_info)
    chat_info = copy.deepcopy(func_call_template)
    user_in = random.choice(task_process_run_info) if "zh" == lang_info else random.choice(task_process_run_info_en)
    in_process_name = random.choice(process_name) if "zh" == lang_info else random.choice(process_name_en)
    ack_task_call_info = copy.deepcopy(ack_tool_exec_process_info)
    chat_info["tools"] = "[" + str(exec_process) + "]"

    if "num" not in user_in:
        ack_task_call_info[0]["arguments"].pop("num")
        # del ack_task_call_info[0]["parameters"]["num"]
    else:
        ack_task_call_info[0]["arguments"]["num"] = number
    ack_task_call_info[0]["arguments"]["name"] = in_process_name

    ans_task_call_info = random.choices(exec_result, weights=weights, k=1)[0]
    # ans_task_call_info = random.choice(exec_result)
    ans_task_call_str = str(ans_task_call_info).replace("'", '"')
    summary_info = random.choice(ok_summary_task_info) if "success" in ans_task_call_str else random.choice(ng_summary_task_info)
    if "en" == lang_info:
        summary_info = random.choice(ok_summary_task_info_en) if "success" in ans_task_call_str else random.choice(ng_summary_task_info_en)

    user_in = user_in.replace("{num}", str(repeat_id)).replace("{transport_plan_id}", "默认").replace("{task_process_id}", in_process_name)
    chat_info["conversations"][0]["value"] = user_in
    chat_info["conversations"][1]["value"] = str(ack_task_call_info).replace("'", '"')
    chat_info["conversations"][2]["value"] = ans_task_call_str
    chat_info["conversations"][3]["value"] = summary_info

    return chat_info, in_process_name, number


def create_follow_execute_data():
    user_info = []
    data_list = []
    num = random.randint(1, 5)
    tool_set = set()
    for i in range(num):
        user_in = random.choice(gen_task_info)
        user_info.append(user_in)

        # if "get_pos_id" in user_in and "put_goods_id" in user_in:
        #     data, get_id, put_id = create_get_put_data()
        #     get_id_info, put_id_info = str(get_id)+"号库位", str(put_id)+"号库位"
        #     user_in = user_in.replace("{get_pos_id}", str(get_id_info)).replace("{put_goods_id}", str(put_id_info))

        if "get_pos_id" in user_in:
            data, get_id = create_get_goods_data()
            get_id_info = str(get_id) + "号库位"
            user_in = user_in.replace("{get_pos_id}", str(get_id_info))

        elif "put_goods_id" in user_in:
            data, put_id = create_put_goods_data()
            put_id_info = str(put_id)+"号库位"
            user_in = user_in.replace("{put_goods_id}", str(put_id_info))

        else:
            data, charge_id = create_exec_charge_data()
            charge_id_info = str(charge_id) + "号库位"
            user_in = user_in.replace("{charge_pos_id}", str(charge_id_info))

        ans_gen_info = random.choice(ans_gen_task_info)
        ask_run_info = random.choice(ask_to_run_generated_task)
        sys_ask_dict = {"from": "gpt", "value": ans_gen_info}
        usr_ext_rsp_dict = {"from": "human", "value": ask_run_info}
        # sys_ans_dict = {"role": "assistant", "content": ans_gen_info}
        # usr_ext_rsp_dict = {"role": "user", "content": ask_run_info}

        data["conversations"][0]["value"] = user_in
        if len(data["conversations"]) != 4:
            del data["conversations"][1:3]

        data["conversations"].insert(1, sys_ask_dict)
        data["conversations"].insert(2, usr_ext_rsp_dict)

        data_list.append(data)

    for i in range(len(data_list)):
        tool_set.add(data_list[i]["tools"])

    tools_str = "["
    tool_list = list(tool_set)
    for i in range(len(tool_list)):
        tools_str += tool_list[i][1:-1]
        if i != len(tool_list) - 1:
            tools_str += ","
        else:
            tools_str += "]"

    merge_data = dict({"conversations": [], "tools": tools_str})
    for i in range(len(data_list)):
        if i != len(data_list) - 1 :
            merge_data["conversations"].extend(data_list[i]["conversations"][0:2])
        else:
            merge_data["conversations"].extend(data_list[i]["conversations"][0:3])

    for j in range(len(data_list)):
        ans_str = str(data_list[j]["conversations"][4])
        if "fail" in ans_str:
            merge_data["conversations"].extend(data_list[j]["conversations"][3:])
            break

        if j != len(data_list) - 1:
            merge_data["conversations"].extend(data_list[j]["conversations"][3:5])
        else:
            merge_data["conversations"].extend(data_list[j]["conversations"][3:])

    return merge_data


def create_ctrl_data(lang_info, weights=[0.5, 0.5]):
    # lang_info = random.choice(lang_set)
    num = random.randint(0, 4)
    cmd_type = list(cmd_control_info[num].keys())[0] if "zh" == lang_info else list(cmd_control_info_en[num].keys())[0]
    cmd_user = random.choice(cmd_control_info[num][cmd_type]) if "zh" == lang_info else random.choice(cmd_control_info_en[num][cmd_type])

    # cmd_user = random.choice(cmd_info[cmd_type])

    cmd_id = ""
    if "zh" == lang_info:
        for info in cmd_control_map_zh:
            if list(info.keys())[0] == cmd_type:
                cmd_id = info[cmd_type]
                break
    else:
        cmd_id = cmd_type

    chat_info = copy.deepcopy(func_call_template)
    ask_cmd_call_info = copy.deepcopy(ack_tool_ctrl_info)
    # ans_task_call_info = random.choice(exec_result)
    ans_task_call_info = random.choices(exec_result, weights=weights, k=1)[0]
    ans_task_call_str = str(ans_task_call_info).replace("'", '"')
    summary_info = random.choice(ok_summary_task_info) if "success" in ans_task_call_str else random.choice(ng_summary_task_info)
    if "en" == lang_info:
        summary_info = random.choice(ok_summary_task_info_en) if "success" in ans_task_call_str else random.choice(ng_summary_task_info_en)

    chat_info["tools"] = "[" + str(exec_control) + "]"
    chat_info["conversations"][0]["value"] = cmd_user
    chat_info["conversations"][1]["value"] = str(ask_cmd_call_info).replace("'", '"').replace("{ctrl_name}", cmd_type)
    chat_info["conversations"][2]["value"] = ans_task_call_str
    chat_info["conversations"][3]["value"] = summary_info

    return chat_info, cmd_id


def create_mix_order_data(lang_info):
    # lang_info = random.choice(lang_set)
    user_in = random.choice(ask_mix_order_info) if "zh" == lang_info else random.choice(ask_mix_order_info_en)
    pattern = re.compile(r'\{(\w+)\}')
    order_seq = pattern.findall(user_in)
    if "num" in order_seq:
        order_seq.remove("num")

    tool_set = set()
    merge_data = dict({"conversations": [], "tools": []})

    key_words_info = []
    for i in range(len(order_seq)):
        if "get_pos_id" == order_seq[i]:
            data, get_id = create_get_goods_data(lang_info, weights=[0.9, 0.1])
            get_id_info = str(get_id) + "号库位" if "zh" == lang_info else "location " + str(get_id)
            if len(data["conversations"]) == 4:
                del data["conversations"][0]
            else:
                del data["conversations"][0:3]

            tool_set.add(data["tools"][1:-1])
            if "success" not in data["conversations"][1]["value"] and i != len(order_seq) - 1:
                merge_data["conversations"].extend(data["conversations"])
            elif i == len(order_seq) - 1:
                merge_data["conversations"].extend(data["conversations"])
            else:
                merge_data["conversations"].extend(data["conversations"][:-1])
            # merge_data["conversations"].extend(data["conversations"])
            key_words_info.append(get_id_info)

        elif "put_goods_id" == order_seq[i]:
            data, put_id = create_put_goods_data(lang_info, weights=[0.9, 0.1])
            put_id_info = str(put_id) + "号库位" if "zh" == lang_info else "location " + str(put_id)
            if len(data["conversations"]) == 4:
                del data["conversations"][0]
            else:
                del data["conversations"][0:3]

            tool_set.add(data["tools"][1:-1])
            if "success" not in data["conversations"][1]["value"] and i != len(order_seq) - 1:
                merge_data["conversations"].extend(data["conversations"])
            elif i == len(order_seq) - 1:
                merge_data["conversations"].extend(data["conversations"])
            else:
                merge_data["conversations"].extend(data["conversations"][:-1])
            # merge_data["conversations"].extend(data["conversations"])
            key_words_info.append(put_id_info)

        elif "control_type" == order_seq[i]:
            data, cmd_id = create_ctrl_data(lang_info, weights=[0.9, 0.1])
            if len(data["conversations"]) == 4:
                del data["conversations"][0]
            else:
                del data["conversations"][0:3]

            tool_set.add(data["tools"][1:-1])
            if "success" not in data["conversations"][1]["value"] and i != len(order_seq) - 1:
                merge_data["conversations"].extend(data["conversations"])
            elif i == len(order_seq) - 1:
                merge_data["conversations"].extend(data["conversations"])
            else:
                merge_data["conversations"].extend(data["conversations"][:-1])
            # merge_data["conversations"].extend(data["conversations"])
            key_words_info.append(cmd_id)

        elif "charge_pos_id" == order_seq[i]:
            data, charge_id = create_exec_charge_data(lang_info)
            charge_id_info = str(charge_id) + "号库位" if "zh" == lang_info else "location " + str(charge_id)
            if len(data["conversations"]) == 4:
                del data["conversations"][0]
            else:
                del data["conversations"][0:3]

            tool_set.add(data["tools"][1:-1])
            if "success" not in data["conversations"][1]["value"] and i != len(order_seq) - 1:
                merge_data["conversations"].extend(data["conversations"])
            elif i == len(order_seq) - 1:
                merge_data["conversations"].extend(data["conversations"])
            else:
                merge_data["conversations"].extend(data["conversations"][:-1])
            # merge_data["conversations"].extend(data["conversations"])
            key_words_info.append(charge_id_info)

        elif "task_process_id" == order_seq[i]:
            data, proc_name, num = create_task_process_data(lang_info, weights=[0.8, 0.2])
            info = user_in.replace("{num}", str(num))
            user_in = info

            if len(data["conversations"]) == 4:
                del data["conversations"][0]
            else:
                del data["conversations"][0:3]

            tool_set.add(data["tools"][1:-1])
            if "success" not in data["conversations"][1]["value"] and i != len(order_seq) - 1:
                merge_data["conversations"].extend(data["conversations"])
            elif i == len(order_seq) - 1:
                merge_data["conversations"].extend(data["conversations"])
            else:
                merge_data["conversations"].extend(data["conversations"][:-1])

            key_words_info.append(proc_name)
        # elif "special_query" == order_seq[i]:
        #     data = create_fork_query_data()
        #     info = user_in.replace("{special_query}", "")
        #     user_in = info
        #     pass

    for k in range(len(key_words_info)):
        user_str = user_in.replace("{"+order_seq[k] + "}", key_words_info[k])
        user_in = user_str
    user_info = {"from": "human", "value": user_in}
    merge_data["conversations"].insert(0, user_info)

    for k in range(len(merge_data["conversations"])):
        if merge_data["conversations"][k].get("from") == "observation" and "fail" in merge_data["conversations"][k].get("value"):
            merge_data["conversations"] = merge_data["conversations"][:k+2]
            break

    tool_list = []
    for info in list(tool_set):
        tool_list.append(eval(info))
    merge_data["tools"] = str(tool_list).replace("'", '"')

    return merge_data


if __name__ == "__main__":
    num_per_task = 200
    chat_list = []
    # generate introduction query info
    for i in range(200):
        prob = random.uniform(0, 1)
        lang_info = "en" if prob > 0.2 else "zh"
        info = create_self_query_data(lang_info)  # only english
        chat_list.append(info)

    # generate purpose query info
    for i in range(40):
        info = create_purpose_query_data("en")
        chat_list.append(info)

    # generate agv location query info
    for i in range(10):
        info = create_agv_loc_query_data("en")
        chat_list.append(info)

    # generate performance query info
    for i in range(2000):   # 73
        prob = random.uniform(0, 1)
        lang_info = "en" if prob > 0.2 else "zh"
        # lang_info = random.choice(lang_set)
        info = create_common_query_data(lang_info)
        chat_list.append(info)

    # # generate agv task query info
    # for i in range(50):
    #     info = create_agv_task_query_data("en")
    #     chat_list.append(info)

    # generate fork state query info
    for i in range(500):
        prob = random.uniform(0, 1)
        lang_info = "en" if prob > 0.2 else "zh"
        # lang_info = random.choice(lang_set)
        info = create_status_query_data(lang_info)
        chat_list.append(info)

    # generate agv operation state query info
    for i in range(100):
        info = create_agv_operate_query_data("en")
        chat_list.append(info)

    #  generate charge info
    for i in range(100):
        # lang_info = random.choice(lang_set)
        prob = random.uniform(0, 1)
        lang_info = "en" if prob > 0.2 else "zh"
        info, _ = create_exec_charge_data(lang_info)
        chat_list.append(info)

    # generate get goods task info
    for i in range(1000):
        # lang_info = random.choice(lang_set)
        prob = random.uniform(0, 1)
        lang_info = "en" if prob > 0.2 else "zh"
        info, _ = create_get_goods_data(lang_info)
        chat_list.append(info)

    # generate put goods task info
    for i in range(1000):
        # lang_info = random.choice(lang_set)
        prob = random.uniform(0, 1)
        lang_info = "en" if prob > 0.2 else "zh"
        info, _ = create_put_goods_data(lang_info)
        chat_list.append(info)

    # generate get and put task info
    for i in range(500):
        # lang_info = random.choice(lang_set)
        prob = random.uniform(0, 1)
        lang_info = "en" if prob > 0.2 else "zh"
        info, _, _ = create_get_put_data(lang_info)
        chat_list.append(info)

    # generate task process info
    for i in range(1000):
        # lang_info = random.choice(lang_set)
        prob = random.uniform(0, 1)
        lang_info = "en" if prob > 0.2 else "zh"
        info, proc_name, num = create_task_process_data(lang_info)
        chat_list.append(info)

    # # create all task, and then run.
    # for i in range(num_per_task):
    #     info = create_follow_execute_data()
    #     chat_list.append(info)

    # generate cmd control info
    for i in range(1000):
        # lang_info = random.choice(lang_set)
        prob = random.uniform(0, 1)
        lang_info = "en" if prob > 0.2 else "zh"
        data, cmd_id = create_ctrl_data(lang_info)
        chat_list.append(data)

    #generate mix order info
    for i in range(500):
        # lang_info = random.choice(lang_set)
        prob = random.uniform(0, 1)
        lang_info = "en" if prob > 0.2 else "zh"
        data = create_mix_order_data(lang_info)
        chat_list.append(data)

    random.shuffle(chat_list)
    filename = 'chat_data.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(chat_list, f, ensure_ascii=False, indent=2)

    # mix get, put, charge task

    # json_lines = ''
    # for item in chat_list:
    #     json_lines += json.dumps(item, ensure_ascii=False) + '\n'
    #
    # with open(filename, 'w', encoding='utf-8') as f:
    #     f.write(json_lines)
    print("Finish Synthetic Data Genereation\n")