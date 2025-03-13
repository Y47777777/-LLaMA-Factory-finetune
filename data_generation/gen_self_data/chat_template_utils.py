common_chat_template ={"type": "chatml", "messages": [{"role": "system", "content": "你是Vision Nav智能语音助手."}, {"role": "user", "content": "{user_chat_info}"}, {"role": "assistant", "content": "{sys_answer_info}"}], "source": "self-made"}


#你可以实现外部tools工具调用，如：
########################################## introduce yourself #####################################################################
self_query_info_zh = [
    "请介绍一下你自己。",
    "给我说说你自己的情况吧。",
    "你是谁呀？",
    "你能向我自我介绍一下吗？",
    "请说出你的故事？",
    "你是谁？",
    "给我讲讲你自己吧。",
    "你来介绍一下自己呗。",
    "跟我分享一下你的情况。",
    "说说你自己的一些情况。",
    "请你做个自我介绍。",
    "你叫什么名字呀？",
    "你是哪位呀？",
    "你到底是谁呀？",
    "你叫啥呀？",
    "你是何人呀？",
    "你叫什么来着？",
    "你叫什么名字呢？"
]

self_query_info_en = [
    "Please introduce yourself",
    "Tell me something about yourself",
    "Introduce yourself.",
    "Tell me about yourself.",
    "Who are you?",
    "Can you introduce yourself to me?",
    "What are you like?",
    "What’s your story?",
    "What's your name?"
    "Give me an introduction."
    "Give me an overview of who you are."
    "How would you introduce yourself?"
]

ans_self_query_info_zh = [
    "嗨！我是未来, 由未来机器人开发的人工智能助手。我能帮助你完成各种任务，比如搬运货物、报告状态等。今天我能为你做些什么呢？",
    "我是人工智能助手,我叫未来，设计用于处理叉车作业任务，如搬运货物、检查状态以及协助各种任务流程。",
    "我叫未来，是为你设计的，旨在帮助你完成日常任务，让你的工作更轻松。我的设计专注于执行像搬运货物、检查车体状态等工作。",
    "嘿！我是未来机器人公司打造的AI助手，擅长各种任务，例如移动货物、汇报车体情况等。今天需要我帮忙做点啥？",
    "我是未来机器人公司研发的智能助手，能协助你处理诸多事务，像移动货物、车体控制等。今日我能为你效劳什么呢？",
    "您好，我是未来，一款由未来机器人打造的智能助手。在叉车作业方面，我能够为您提供全方位的帮助。请问您现在有什么需要我协助的吗？",
    "嗨，我是未来，由未来机器人研发的人工智能助手。如果您有叉车作业相关的事宜需要帮忙，尽管告诉我，我很乐意为您服务。",
    "你好呀，我是未来，未来机器人开发的人工智能助手哦。叉车作业的任务交给我就行，您看您现在有什么要我做的？",
    "您好，我是未来，来自未来机器人的智能助手。在叉车作业这块，我能帮您搞定很多事情。您现在需要我做点啥呢？",
    "您好，我是未来机器人开发的人工智能助手。如果您有取货、放货等事务需要帮忙，就尽管吩咐我，我随时待命。",
]

ans_self_query_info_en = [
    "Hi! I'm Visionnav, an AI assistant developed by VisionNav corporation. I can help you with various tasks such as moving cargo, reporting status, and more. How can I assist you today?",
    "I'm Visionnav, an efficient, precise AI Assistant, and designed to handle repetitive tasks like moving items, checking statuses,and assisting with various workflows.",
    "I'm Visionnav, and created to help you with everyday tasks and make your work easier. My design is focused on performing actions like moving cargo, checking system statuses, and more.",
]

############# purpose and function #########################
ask_purpose_query_info_en = [
    "What are you designed for?",
    "What’s your purpose?",
    "What do you do?",
    "What’s your mission?",
    "Why were you made?",
    "How do you help me?",
    "What are your capabilities",
    "How can you assist me",
    "What's your functionality list?",
    "List all the things you can do.",
    "What support can you offer me?",
    "How do you operate?",
    "How can you serve me?"
]

ans_purpose_query_info_en = [
    "I’m designed to help you automate and manage tasks like transporting goods, checking vehicle status, and assisting with various operations. How can I assist you today?",
    "My purpose is to assist you in completing tasks like moving items, checking status, and executing commands for more efficient operations.",
    "I can help you with tasks like transporting items, reporting vehicle status, and performing repetitive actions to improve workflow efficiency.",
    "My mission is to make your tasks easier by handling repetitive operations, reporting system statuses, and helping with various workflows.",
    "I was made to assist with tasks that require precision and repetition, like moving cargo and managing workflow operations. How can I help?",
    "I can help by performing tasks like transporting cargo, checking AGV status, and automating routine operations that would otherwise take up your time.",
]
################################################# 1. query performence template info #######################################################
do_query_info = [
    "你具备哪些功能",
    "你能帮我完成哪些任务",
    "你能够执行哪些操作",
    "你有哪些能力",
    "你支持哪些命令",
    "你能够进行哪些活动",
    "你有哪些可用的服务",
    "你能够帮我做些什么",
    "你有哪些可以做的事情",
    "你能够处理哪些任务",
]

do_query_info_en = [
    "What are your capabilities?",
    "What tasks can you perform?",
    "What functions do you offer?",
    "What actions can you take?",
    "What services can you provide?",
    "What activities can you engage in?",
    "What operations are you able to execute?",
    "What duties can you fulfill?",
    "What responsibilities can you handle?",
    "What tasks can you manage?",
    "what can you do?",
    "what is your function?",

    "How can you assist me?",
    "How can you help?",
    "Can you tell me what you can do?",
    "What are all your abilities?",
    "What's in your functionality list?",
    "List all the things you can do.",
    "What is your purpose here?",
    "What is your purpose?",
    "What do you do?",
    "How can I use your features?",
    "How can I interact with you?",
    "What kind of help can you provide?",
    "What support can you offer me?",
    "What does your system allow you to do?",
    "What kind of requests can I make to you?",
    "How do you operate?",
    "How can you serve me?",

    "List your functions.",
    "Show me your functions.",
    "What are your features?",
    "What features do you have?",
    "What functions do you have?",
    "List your features.",
    "Can you explain your function?",
    "What kind of tasks are you good at?",

    "What commands can I give you?",
    "What jobs can you handle?",
    "What tasks are you capable of doing?",
    "What kinds of jobs can you perform?",
    "What operations are you programmed for?",
    "What operations can you perform?",
    "What work can you take care of?",
    "What kind of tasks can you execute?",
    "What directions can I give you?",
    "What tasks are you most effective at?",
    "What tasks can I ask you to perform?",
    
    "What services do you offer?",
    "What services are you programmed for?",
    
    "What's your role in this operation?",
    "What's your purpose here?",
    "What is your primary function?",
    "How are you designed to help?",
    
    "What's your skillset?",
    "What are your programmed skills?",
    "Can you explain your skills?",
    "What do you excel at?",
    "How do you perform tasks?",
    "What kind of orders can I issue?",
    "What do you specialize in?",

    "Can you handle complex workflows?",
    "Can you perform detailed task flows, like pick-up and drop-off?",
    "Can you handle customized task flows or scenarios?",
    "Can you manage multiple tasks simultaneously?",
    "Can you manage tasks that require adjustments or changes mid-way?",
    "Can you specialize in performing a series of tasks sequentially?",

    "Are you good at specific tasks?",
    "Are there certain types of jobs you're made for?",
    "Are you specialized in anything in particular?",
    "Are there any tasks you're better at than others?",
    "Are there jobs you're really good at?",
    "Are you designed for certain types of work?",
]

ans_do_query_info = [
	"您好！请告诉我您的需求，我能够协助您完成无人叉车取货、放货、充电等多种任务，并提供车体状态的实时查询功能。",
	"您好！我随时准备帮助您，包括无人叉车执行操作指令(取货、放货和充电)，以及监控及控制车体状态。",
	"您好！我在这里等候您的指令，可以帮您处理AGV取货、放货、充电等任务，并随时向您报告车辆状态。",
	"您好！我的功能包括协助您完成各种AGV任务，如取货、放货、充电，以及车体状态查询和控制。您需要我的帮助吗？",
	"您好！我具备帮助您执行无人叉车取货、放货、充电等任务的能力，同时能够提供车体状态的查询服务。",
	"您好！我在这里为您提供全方位的智能语音帮助，包括但不限于取货、放货、充电任务的创建和执行，以及车体状态的查询。",
	"您好！我能够按照您的语音指示，帮助您完成取货、放货、充电等任务，并随时上报车体状态信息。",
	"您好！我在这里就是为了协助您，无论是执行取货、放货、充电任务，或是查询车体状态，我都乐意效劳。",
	"您好！我随时待命，准备帮助您完成包括取货、放货、充电在内的各项任务，并提供车体状态的即时查询。",
	"您好！我的功能旨在帮助您，无论是下发取货、放货、充电任务，还是控制和查询车体状态，我都在这里为您服务。",
]

ans_do_query_info_en = [
  "Hello! I'm here to assist you with a variety of tasks, such as dispatching orders for picking up, put, and charging AGV, as well as managing and checking the status of the vehicle. How may I serve you?",
  "I can aid you in completing numerous tasks, including picking up and putting load, and charging automated guided vehicle, executing tasks, and controlling AGV's condition. What can I do for you?",
  "Hi there! I'm equipped to help with a range of tasks, like sending missions for picking up, putting, controlling and charging, and querying the vehicle's status. What assistance do you need?",
  "Hello! I can support you in accomplishing various tasks, such as dispatching orders for getting, placing, and charging, and handling and inspecting the vehicle's state. What do you need help with?",
  "Good day! I am ready to assist you with an array of tasks, including picking up and placing load, and charging forklift, implementing these directives, and overseeing and scrutinizing the forklift's state of charge. What can I assist you with?",
  "Hey there! I can lend a hand with a multitude of tasks, like devising and transmitting commands for acquiring, delivering, executing these commands, and supervising the AGV's status. What task do you require my help for?",
  "Salutations! I have the ability to help with a broad spectrum of tasks, such as establishing and dispatching orders for acquiring and placing cargo, and replenishing energy for forklift, and querying the vehicle's condition. How may I be of service?",
  "Hello! I'm at your service to help with a variety of tasks, like getting and putting cargo, and charging forklift, performing tasklist. What can I help you with now?",
  "Hi! I can provide assistance for a host of tasks, such as picking up and placing cargo, and powering up automated guided vehicle(AGV), and controlling and checking the vehicle's status. What help do you need?",
  "Greetings! I am capable of aiding with a wide range of tasks, including creating and distributing orders for getting and putting load, and recharging forklift. How can I assist you?",

  "Hi! I can assist you with various tasks, such as executing pick-up, drop-off, and other task flows. You can also use me to control the robot, like making it stop or continue its tasks. Additionally, I can query the robot's status information. How can I assist you today?",
  "Hi! I can help you execute tasks such as pick-up, drop-off, and more. I can also control the robot's actions, like making it stop or resume its tasks. Plus, I can retrieve the robot's status information for you. Let me know what you'd like me to do!",
  "Hi! I am capable of executing various tasks such as pick-up, drop-off, and following specified task flows. You can also instruct me to pause or resume tasks, and I can provide you with the robot's status at any time. What task would you like me to perform?",
  "Hi! I offer services such as task execution, robot control, and status querying. You can have me carry out tasks like pick-up or drop-off, and I can also pause or continue tasks as needed. I am here to help, so feel free to tell me what you need!",
  "Hi! My purpose is to assist with managing robotic tasks such as pick-up, drop-off, and task flow execution. I can also control the robot's operations, like making it stop or resume, and I can provide status updates. How can I help you today?",
  "Hi! I am skilled at executing tasks such as pick-up, drop-off, and custom task flows. I can also control the robot's movements, pause or resume tasks, and retrieve its status information. How can I assist you with these skills?",
  "Hi! You can instruct me to execute tasks like pick-up, drop-off, or other flows. I can also control the robot's actions, such as stopping or resuming tasks, and I can retrieve the robot's status information. Just let me know what you need!",
  "Hi! I operate by executing tasks such as pick-up, drop-off, and other task flows. You can control the robot through me by making it stop or continue its tasks. Additionally, I can query the robot's status to ensure everything is running smoothly.",
  "Hi! I specialize in task execution, such as pick-up, drop-off, and other task flows. I also excel in  controlling the robot's actions, like pausing or resuming tasks, and I can retrieve status updates to ensure everything is functioning as it should. How can I assist you today?",
  "Hi! Yes, I can handle complex workflows and manage detailed task flows like pick-up and drop-off.So,if you've got something in mind, just let me know, and I will handle it!",
  "Hi! Yes, I am specialized in tasks such as pick-up, drop-off, and specific operational flows. I am also designed to control the robot's actions, such as stopping or resuming tasks,. If you have a particular task in mind, I can adapt to fulfill your needs",

]

############################## query AGV location ####################################
ask_agv_loc_query = [
    "Where is the AGV right now?",
    "Where exactly is the AGV right now?",
    "Where is the AGV currently located?",
]

ans_agv_loc_query = [
    "the agv is here. What task would you like to perform?",
    "I'm here. What task would you like to perform?",
    "I'm here, can you hear my voice? What do you need me to do for you",
]


######################### query agv running ###################################
ask_agv_operate_status = [
    "Is the AGV operational?",
    "Is the AGV active?",
    "Is AGV online?",
    "Is AGV on?",
    "Is AGV working?",
    "Is the AGV operational right now?",
    "Is the AGV online?",
    "Is the AGV active at the moment?",
    "Is the AGV still running?",
    "Is the AGV turned on?",
]

ans_agv_operate_status = [
    "Yes, the AGV is operational and is currently in {car_status_info} state. Its battery is at {num}%. The AGV is handling {agv_task_type} task right now",
    "Yes, the AGV is active and is currently in {car_status_info} state. Its battery is at {num}%. The AGV is handling {agv_task_type} task right now",
    "Yes, the AGV is online and at {car_status_info} stage. It has {num}% battery remaining. The AGV is handling {agv_task_type} task right now",
    "Yes, the AGV is turned on and at {car_status_info} stage. Its battery is at {num}%. The AGV is handling {agv_task_type} task right now",
    "Yes, the AGV is currently working. It's in {car_status_info} state mode with {num}% battery remainin. The AGV is handling {agv_task_type} task right now",
    "Yes, the AGV is operational and is in {car_status_info} state. Its battery is currently {num}%. The AGV is handling {agv_task_type} task right now",
    "Yes, the AGV is active and at {car_status_info} stage. The battery level is {num}%. The AGV is handling {agv_task_type} task right now",
    "Yes, the AGV is still running in {car_status_info} state. Battery level is {num}%. The AGV is handling {agv_task_type} task right now",
    "Yes, the AGV is turned on and at {car_status_info} stage. Its battery is at {num}%. The AGV is handling {agv_task_type} task right now",
]

################################# agv task query info ################################################
# ask_agv_task_query = [
#     "What's the progress of the AGV?",
#     "What's the AGV doing?",
#     "What task is the AGV handling right now",
#     "What activity is the AGV performing?",
#     "What's the AGV's current activity?",
#     "What is the AGV doing now?",
#     "What operation is the AGV running?",
#     "What's the AGV up to?",
#     "What progress has the AGV made?",
#     "What's happening with the AGV at this moment?",
# ]
#
# ans_agv_task_query = [
#     "The AGV is currently managing the {agv_task_type} task.",
#     "At this moment, the AGV is engaged in processing the {agv_task_type} task.",
#     "The AGV is in the midst of addressing the {agv_task_type} task at hand.",
#     "The AGV is handling {agv_task_type} task right now.",
#     "The forklift is handling {agv_task_type} task right now.",
# ]

################################################# 2. query car template info #######################################################
car_query_info = [
    "请告诉我叉车当前电量是多少？",
    "叉车当前在执行什么任务？",
    "叉车现在在干什么？",
    "请上报叉车当前的电量和运行状态！",
    "请报告车体当前状态",
    "我想知道车体的状态",
    "请提供车体状态信息",
    "车体现在是什么状态",
    "查询一下车辆的当前状态",
    "请告诉我车辆的状态",
    "叉车当前电量多少，在执行什么任务",
    "我需要知道车体的状态",
    "请更新车体状态",
    "车体状态查询",
]

car_query_info_en = [
    "show me the AGV's condition.",
    "report the status of the forklift.",
    "tell me the AGV's current state.",
    "tell me the AGV's state of charge.",
    "Could you please tell me the AGV's operating status.",
    "show me the forklift's status details.",
    "help me query the AGV's status.",
    "display the AGV's status information.",
    "present the forklift's activity status.",
    "query the AGV's state information",

    "Tell me AGV status",
    "What's the current AGV status?",
    "Give me a status update.",
    "Report the AGV status.",
    "Check AGV status.",
    "Can you tell me the AGV's status?",
    "Check on the AGV status.",
    "Can you confirm if the AGV is active?",
    "Can you report on the AGV's progress?",

    "Can you check the AGV's current task?",
    "Give me a status update on the AGV.",
    "Report the AGV's activity.",
    "Check if the AGV is on.",

    "What's the progress of the AGV?",
    "What's the AGV doing?",
    "What task is the AGV handling right now",
    "What activity is the AGV performing?",
    "What's the AGV's current activity?",
    "What is the AGV doing now?",
    "What operation is the AGV running?",
    "What's the AGV up to?",
    "What progress has the AGV made?",
    "What's happening with the AGV at this moment?",



]

ok_ans_car_query_info = [
    "当前车辆的电量是{num}%。它现在正在处于{car_status_info}状态, 车辆正在执行{agv_task_type}任务",
	"车辆剩余电量显示为{num}%。目前操作状态：{car_status_info}状态, 车辆正在执行{agv_task_type}任务。",
	"请注意，车辆电量现在是{num}%。任务状态情况：处于{car_status_info}阶段。车辆正在执行{agv_task_type}任务",
	"车辆当前电量达到了{num}%。现在车辆运行状态为{car_status_info}状态。车辆正在执行{agv_task_type}任务",
	"提示：车辆电量为{num}%。当前运行状态更新为{car_status_info}状态。车辆正在执行{agv_task_type}任务",
	"车辆电量信息更新：当前为{num}%。车辆状态是：{car_status_info}状态。车辆正在执行{agv_task_type}任务",
	"检查车辆电量，现在有{num}%的电量。任务进展：车辆处于{car_status_info}状态。车辆正在执行{agv_task_type}任务",
	"车辆电量报告：{num}%的电量剩余。任务状态：当前在{car_status_info}状态。车辆正在执行{agv_task_type}任务",
	"当前车辆电量显示为{num}%。任务状态：车辆正在处于{car_status_info}状态。车辆正在执行{agv_task_type}任务",
	"车辆电量监控：{num}%电量可用。任务动态：车辆正处于{car_status_info}状态。车辆正在执行{agv_task_type}任务",
]

ok_ans_car_query_info_en = [
    "The present AGV's power is at {num}%. the current status of the AGV is {car_status_info} state.The AGV is handling {agv_task_type} task right now",
    "The forklift's state of charge stands at {num}%. The forklift is currently at {car_status_info} stage.The AGV is handling {agv_task_type} task right now",
    "The current AGV's energy is {num}%. It is now in {car_status_info} state.The AGV is handling {agv_task_type} task right now",
    "The automated guided vehicle's current battery is {num}%. It is at the moment experiencing {car_status_info} state.The AGV is handling {agv_task_type} task right now",
    "The forklift's electrical level is {num}%. It is currently at {car_status_info} stage.The AGV is handling {agv_task_type} task right now",
    "The AGV's charge rate is {num}%. It is now at {car_status_info} phase.The AGV is handling {agv_task_type} task right now",
    "The SOC of the AGV is {num}%. It is now addressing {car_status_info} work.The AGV is handling {agv_task_type} task right now",
    "The forklift's energy level is {num}%. It is now at {car_status_info} stage.The AGV is handling {agv_task_type} task right now",
    "The AGV's power level is {num}%. It is currently in{car_status_info} state.The AGV is handling {agv_task_type} task right now",
    "The forklift's state of charge is at {num}%. forklift is now in {car_status_info} state.The AGV is handling {agv_task_type} task right now",

    "The AGV is currently at {car_status_info} stage and active. Its battery level is {num}%.The AGV is handling {agv_task_type} task right now",
    "The AGV is currently in {car_status_info} state, with {num}% battery left.The AGV is handling {agv_task_type} task right now",
    "Yes, the AGV is on and in {car_status_info} state. Battery is at {num}%.The AGV is handling {agv_task_type} task right now",


]

ok_summary_task_info = [
    "当前任务已成功完成，特此通知。",
    "请留意，当前任务已经圆满结束。",
    "任务已完成，请及时查收。",
    "通知您，当前任务已经顺利达成。",
    "请知晓，我们已经成功结束了当前的任务。",
    "已经顺利完成任务，请及时了解。",
    "任务已经结束了，请及时关注。",
    "通知您，当前任务已经完成。",
    "请留意，我们已经完成了当前的任务。",
    "任务已经完成，请及时确认。",
]

ok_summary_task_info_en = [
    "Please note that the current task has been completed.",
    "the present order is finished.",
    "Attention: The task is done.",
    "The current mission is successful.",
    "The present task is executed.",
]

# ok_get_summary_task_info = [
#     "取货任务已成功完成，特此通知。",
#     "请留意，取货任务已经圆满结束。",
#     "取货任务已完成，请及时查收。",
#     "通知您，取货任务已经顺利达成。",
#     "请知晓，我们已经成功结束了取货的任务。",
#     "已经顺利完成取货任务，请及时了解。",
#     "取货任务已经告一段落，请及时关注。",
#     "通知您，取货任务已经彻底完成。",
#     "请留意，我们已经完成了取货的任务。",
#     "取货任务已经完成，请及时确认。",
# ]

ng_get_summary_task_info = [
    "取货任务未能成功完成，需要分析失败的原因。",
    "取货的任务未能达成，请分析失败的原因。",
    "取货任务执行过程中出现了失败，请进行原因分析。",
    "取货任务未能如预期进行，需要对失败原因进行探究。",
    "取货任务执行结果不理想，请分析原因以找出问题所在。",
    "取货任务未能成功，请人工介入并分析原因。",
    "取货任务执行失败，需要深入分析原因。",
    "取货任务未能顺利完成，请分析原因以便采取相应措施。",
    "取货任务执行结果不佳，请检查各种参数配置。",
    "取货任务未能达到预期目标，请分析失败原因以改进。",
]

ng_get_summary_task_info_en = [
    "The task of picking up load was not accomplished; please investigate the cause of failure.",
    "The mission to pick up cargo did not succeed; analyze the reasons for the setback.",
    "The objective of picking up cargo was not met; please dissect the factors contributing to the failure.",
    "The goal of getting load was not reached; examine the origins of the unsuccessful attempt.",
    "The purpose of picking up cargo was not fulfilled; look into the reasons behind the breakdown.",
    "The job of picking up load was not realized; please deconstruct the elements that led to the failure.",
    "The assignment to get goods was not completed; evaluate the causes of the collapse.",
    "The operation to collect cargo was not achieved; please analyze the reasons for the malfunction.",
    "The aim to acquiring load was not realized; explore the causes of the failure to succeed.",
]

ng_summary_task_info = [
    "任务未能成功完成，需要分析失败的原因。",
    "目前的任务未能达成，请分析失败的原因。",
    "任务执行过程中出现了失败，请进行原因分析。",
    "任务未能如预期进行，需要对失败原因进行探究。",
    "任务执行结果不理想，请分析原因以找出问题所在。",
    "任务未能成功，分析失败的原因至关重要。",
    "任务执行失败，需要深入分析原因。",
    "任务未能顺利完成，分析原因以便采取相应措施。",
    "任务执行结果不佳，进行原因分析是当务之急。",
    "任务未能达到预期目标，分析失败原因以改进。",
]

ng_summary_task_info_en = [
    "The mission was not successfully accomplished; it is necessary to analyze the reasons for the failure.",
    "The task failed to be completed successfully; there is a need to examine the causes of the breakdown.",
    "The assignment did not reach a successful conclusion; it's essential to investigate the factors behind the malfunction.",
    "The job was not fulfilled as planned; it's crucial to dissect the origins of the setback.",
    "The operation was unsuccessful in its execution; we must look into the reasons for the collapse.",
    "The goal was not achieved as anticipated; it's vital to evaluate the triggers of the unsuccessful outcome.",
    "The work was not completed successfully; it's necessary to study the reasons for the lack of success.",
    "The activity did not result in a successful outcome; there is a requirement to scrutinize the causes of the error.",
]

task_status_info = [
    "空闲", "取货", "放货", "移动", "充电", "未知", "移动货叉", "检测托盘", "扫描二维码", "执行脚本",
]
task_status_info_en = [
    "idle", "picking up", "putting", "moving", "unknown", "adjust fork", "detect pallet", "scan QR code", "run script",
]

car_status_info = ["未知","初始化","待命","自动运行","定位矫正","自动状态","异常","休眠","关机","开机自检状态","手工自检","行驶","装卸货物","卸载货物","移动货叉","检查托盘","扫描二维码","充电","脚本任务"]
car_status_info_en = ["Unknown","Prepare","Standby","Auto Running","Adjust","Manual","Breakdown","sleep","Shutdown","Self Check","Manual self check","movement","loading","unloading","move lift","detect pallet","scan code","charge battery","run script procedule"]



#task_type_info = []

################################################# 3. charge template info #######################################################
charge_info = [
    "充电",
    "去充电",
    "帮忙给叉车充电",
    "请为车辆充电",
    "车辆需要充电",
    "执行车辆充电任务",
    "请准备给车充电",
    "请启动车辆充电",
    "请帮我安排车辆充电",
    "请进行车辆充电操作",

    "请移动到{charge_pos_id}以进行充电操作。",
    "导航至{charge_pos_id}开始充电过程。",
    "请到{charge_pos_id}执行电池充电。",
    "向{charge_pos_id}出发，准备充电。",
    "移步至{charge_pos_id}进行充电动作。",
    "请前往{charge_pos_id}以启动充电。",
    "请到{charge_pos_id}处进行充电。",
    "去{charge_pos_id}充电"
]

charge_info_en = [
    "please charge for forklift",
    "assist with charging the forklift",
    "Please aid in charging the AGV.",
    "lend a hand with the battery top-up of the forklift.",
    "support in replenishing the power of the lift truck.",
    "start the charging process of the forklift.",
    "charge the AGV",
    
    "Please navigate to {charge_pos_id} to carry out the charging task.",
    "Please move to {charge_pos_id} to start the charging operation.",
    "Make your way to {charge_pos_id} to execute the energy charging task.",
    "Head to {charge_pos_id} to prepare for recharging.",
    "go to {charge_pos_id}, and then charge the forklift",
    "Travel to {charge_pos_id} to run the charge mission.",
    
]

ask_charge_id_info = [
	"请提供充电库位的编号。",
	"请输入充电库位的位置。",
	"请告诉我充电库位的ID。",
	"请确认充电库位的ID号。",
	"请提供用于充电的库位ID。",
	"请指定充电库位的ID。",
	"请输入需要充电的库位ID。",
	"请告知充电库位的ID。",
	"请补充充电库位的ID信息。",
]

ask_charge_id_info_en = [
  "Please provide the identification number for the charging station.",
  "Kindly share the number for the charging location.",
  "Could you give me the number of the battery charging spot?",
  "Please supply the reference number for the charging bay.",
  "Kindly furnish the ID for the charging area.",
  "Could you let me know the designation number of the charging point?",
  "Please indicate the number for the electric charging zone.",
  "Kindly provide the locator number for the charging facility.",
  "Could you share the numeric identifier for the charging dock?",
  "Please give me the number for the power charging station.",
]

ans_charge_id_info = [
  "充电位置为{charge_pos_id}",
	"充电位置已指定为{charge_pos_id}。",
	"{charge_pos_id}将用作充电点。",
	"充电将在库位{charge_pos_id}进行。",
	"{charge_pos_id}被选为充电库位。",
	"充电库位已确认为{charge_pos_id}。",
	"{charge_pos_id}是指定的充电库位。",
	"{charge_pos_id}",
]

ans_charge_id_info_en = [
  "The charging station is located at {charge_pos_id}.",
  "charge at the position designated as {charge_pos_id}.",
  "The charging spot is identified by the number {charge_pos_id}.",
  "The charging bay is specified by {charge_pos_id}.",
  "The charging point is indicated with {charge_pos_id}.",
  "The charging location is numbered {charge_pos_id}.",
  "The battery charge area corresponds to {charge_pos_id}.",
  "The charging dock can be found at {charge_pos_id}.",
  "The power charging station is marked by {charge_pos_id}.",
  "The energizing position is coded as {charge_pos_id}.",
]

ok_ans_charge_info = [
	"明白了，正在为您安排车辆前往充电区，充电即将开始，请耐心等待。",
	"收到，车辆正前往充电位进行充电，请您稍候片刻。",
	"好的，已启动车辆至充电位的充电程序，请稍等。",
	"确认，车辆即将到达充电位并开始充电，请您稍候。",
	"正在处理您的充电请求，车辆将很快到达充电位，请稍等一下。",
	"已安排车辆前往充电位，充电任务即将执行，请耐心等待。",
	"车辆正按指示前往充电位，充电操作即将开始，请稍候。",
	"好的，车辆已经接到充电指令，正在前往充电位，请稍候片刻。",
	"已向车辆下发充电任务，它正在前往指定充电位，请稍候。",
]


################################################# 6. get goods template info #######################################################
get_goods_info = [
    "请去{get_pos_id}取货",
    "帮我从{get_pos_id}取货",
    "请执行取货任务",
    "开始取货操作",
    "我要去{get_pos_id}取货",
    "开始执行取货任务",
    "请开始取货任务",
    "执行取货任务",
    "请安排取货",
    "请帮我去{get_pos_id}取货。",
    "帮我执行取货任务，目的地是{get_pos_id}。",
    "我需要取货服务，请前往{get_pos_id}。",
    "请开始取货操作，目标位置是{get_pos_id}，使用{transport_plan_id}搬运方案。",
    "去{get_pos_id}取货，如果可能的话，请按照{transport_plan_id}搬运方案进行。",
    "请帮我去{get_pos_id}取货。",
    "执行取货任务，使用{transport_plan_id}搬运方案。",
    "请立即开始取货流程，目标是{get_pos_id}。",
    "我需要从{get_pos_id}获取货物。",
    "请从{get_pos_id}提取货物。",
    "我需要在{get_pos_id}取货。",
    "从{get_pos_id}获取货物。",
    "请在{get_pos_id}取货。",
    "我需要从{get_pos_id}提取货物。",
    "请在{get_pos_id}获取货物，使用默认搬运方案。",
    "从{get_pos_id}取货。",
    "请在{get_pos_id}获取货物。",
]

get_goods_info_en = [
    "launch the picking up cargo mission.",
    "carry out the pick up load.",
    "perform the picking up load task.",
    "execute the cargo pickup operation.",
    "handle the cargo acquisition assignment.",
    "Please schedule a pick up task.",
    "Could you organize a cargo acquisition?",
    "Kindly plan a cargo picking up task.",
    
    "Could you assist me in getting goods at {get_pos_id}?",
    "Would you help me acquire the cargo at {get_pos_id}?",
    "Assist me in obtaining the cargo at {get_pos_id}, please.",
    "Assist me in performing the cargo picking up task at {get_pos_id}.",
    "Help me carry out the getting cargo mission to {get_pos_id}.",
    "Support me in executing the load pickup operation, with the destination being {get_pos_id}.",
    "Aid me in handling the cargo acquisition assignment at {get_pos_id}.",
    "Please help with the task of getting goods, where the target location is {get_pos_id}.",
    "I require the acquisition of cargo from {get_pos_id}.",
    "I need to get pallet at {get_pos_id}.",
    "It's necessary for me to get the cargo located at {get_pos_id}.",
    "I am in need of picking up the load from {get_pos_id}.",

    "Pick up the load from {get_pos_id}.",
    "Retrieve the cargo from get_pos_id}.",
    "Collect the item from {get_pos_id}.",
    "Take the load from {get_pos_id}.",
    "Pick the item up from {get_pos_id}.",
    "Load the cargo from {get_pos_id}.",
    "Gather the load from {get_pos_id}.",
    "Fetch the cargo from get_pos_id}.",
    "Pick the goods from {get_pos_id}.",
    "Grab the package from {get_pos_id}.",
    "Get the item from {get_pos_id}.",

]

ask_get_goods_pos_id_info = [
  "需要告知取货库位的ID信息",
  "您忘了告知取货库位的ID信息，请补充",
	"请指定您需要叉车取货的具体库位。",
	"告诉我叉车应该前往哪个库位进行取货。",
	"请提供叉车取货任务的目标库位编号。",
	"需要叉车取货，请指示具体的库位位置。",
	"请问取货点是哪一个库位？",
]

ask_get_goods_pos_id_info_en = [
  "Please provide the identification details for the pickup location.",
  "The ID information of the cargo pickup is required.",
  "pickup location identification number is required!",
  "A requirement for the reveal of the cargo pickup spot's ID information.",
  "There's a need to supplement the identifier for the pickup area.",

  "Which storage location is the pickup point?",
  "Could you specify the location for gettting goods?",
  "What is the identification of the cargo storage point?",
  "May I know the storage slot designated for picking up goods?",
  "Please inform me of the cargo collection spot's position.",
]

ans_get_goods_pos_id_info = [
	"叉车的目标取货点是{get_pos_id}。",
	"请叉车到{get_pos_id}进行取货。",
	"{get_pos_id}",
	"前往{get_pos_id}。",
	"{get_pos_id}是叉车执行取货任务的目的地。",
   "库位ID为{get_pos_id}",
   "位置为{get_pos_id}",
]

ans_get_goods_pos_id_info_en = [
  "The forklift's cargo storage point is {get_pos_id}.",
  "The picking up location for the forklift is {get_pos_id}.",
  "The AGV's intended cargo pickup site is {get_pos_id}.",
  "The forklift's purpose-specific pickup spot is {get_pos_id}.",
  "{get_pos_id}",
  "go to {get_pos_id}。",
  "number ID is {get_pos_id}",
  "located at {get_pos_id}",
  
  "{get_pos_id} serves as the destination for the forklift's pickup mission.",
  "The forklift's task of getting goods is aimed at {get_pos_id}.",
  "The designated pickup location for the forklift's pickup operation is {get_pos_id}.",
  "{get_pos_id} is the target site for the forklift's cargo storage location.",
  "The forklift's objective in its acquisition mission is to reach {get_pos_id}.",
]


################################################# 7. put goods template info #######################################################
put_goods_info = [
	"请执行放货任务。",
	"请开始放货任务。",
	"叉车进行放货。",
	"请帮我完成放货操作。",
    "去{put_goods_id}取货",
    "请将货物运送至{put_goods_id}",
    "货物需要送达{put_goods_id}",
    "前往{put_goods_id}放货",
    "请把货物送至{put_goods_id}",
    "请执行送至{put_goods_id}的任务",
    "请安排将货物送至{put_goods_id}",
    "货物送到{put_goods_id}",

    "请将货物运送至{put_goods_id}。",
    "请帮我把货物放到{put_goods_id}。",
    "执行放货任务，目标地点是{put_goods_id}。",
    "请按照{transport_plan_id}搬运方案，将货物运送至{put_goods_id}。",

    "安排放货任务到{put_goods_id}，搬运方案为{transport_plan_id}。",
    "地点是{put_goods_id}，请安排放货任务，使用搬运方案{transport_plan_id}。",
    "安排放货任务到{put_goods_id}，使用搬运方案{transport_plan_id}。",
]

put_goods_info_en = [
    "Please carry out the task of putting pallet.",
    "Kindly perform the operation of putting cargo.",
    "Please execute the mission of placing goods.",
    "Assist in accomplishing the assignment of putting pallet.",
    "Could you facilitate the operation of placing pallet?",
    "please start putting cargo mission",
    "Please assist me in carrying out the goods delivery procedure.",
    "Could you help me execute the cargo unloading process?",

    "Proceed to {put_goods_id} to put the cargo.",
    "Head over to {put_goods_id} for the pallet placement.",
    "Move towards {put_goods_id} to put cargo.",
    "Navigate to {put_goods_id} for the cargo putting.",
    "Make your way to {put_goods_id} to putting cargo.",
    "Schedule a goods delivery task at {put_goods_id}.",
    "Plan a cargo unloading operation to location {put_goods_id}.",
    "Organize a goods placement mission to {put_goods_id}.",
    "The destination is {put_goods_id}, please schedule the goods offloading task.",
    "The location is {put_goods_id}, kindly arrange the cargo unloading duty.",
    "The location is {put_goods_id}, could you organize the cargo putting process?",
    "The position is {put_goods_id}, assist in setting up the product placement operation.",

    "Place load at {put_goods_id}.",
    "Place cargo at {put_goods_id}.",
    "Move the load to {put_goods_id}.",
    "Deliver the cargo to {put_goods_id}.",
    "Place the item at {put_goods_id}.",
    "Transport the load to {put_goods_id}.",
    "Drop the cargo at {put_goods_id}.",
    "Take the load to {put_goods_id}.",
    "Move the package to {put_goods_id}.",
    "Send the cargo to {put_goods_id}.",
    "Put the item at {put_goods_id}.",
    "Deliver the goods to {put_goods_id}.",

]

ask_put_goods_id_info = [
	"请提供放货库位id的详细情况。",
	"我需要了解放货库位id的确切信息。",
	"请说明放货库位的相关情况。",
	"请指示放货库位的准确信息。",
	"请告知放货库位id的具体细节",
    "请补充放货库位的信息",
]

ask_put_goods_id_info_en = [
  "Please supply detailed information about the cargo placement ID.",
  "Kindly supply specifics regarding the cargo putting location identifier.",
  "Could you provide a detailed description of the goods placement area number?",
  "Please offer comprehensive details on the unloading spot number.",
  "Please provide details about the cargo unloading number.",
  "Could you describe the goods placement location?",
]

ans_put_goods_id_info=[
	"放货的库位编号是{put_goods_id}。",
	"放货操作的目标库位已被设定为{put_goods_id}。",
	"叉车前往库位{put_goods_id}进行放货",
	"指定的放货库位编号为{put_goods_id}。",
	"库位{put_goods_id}是本次放货任务的目的地。",
  "{put_goods_id}",
]

ans_put_goods_id_info_en = [
  "The storage location ID for placing goods is {put_goods_id}.",
  "The identifier for the cargo placement is {put_goods_id}.",
  "The putting cargo spot number is designated as {put_goods_id}.",
  "The allocation number for the goods placement area is {put_goods_id}.",
  "The slot ID where to unload the cargo is {put_goods_id}.",
  "The designated storage location identification number is {put_goods_id}.",
  "The specified goods putting location ID is {put_goods_id}.",
  "The assigned cargo placement site number is {put_goods_id}.",
  "The indicated unload placement area number is {put_goods_id}.",
  "The selected cargo offloading spot identifier is {put_goods_id}.",
]

################################################# 8. get_follow_put template info #######################################################
get_put_info_bak = [
    "请先到{get_pos_id}取货，随后将货物送至{put_goods_id}",
    "请在{get_pos_id}取完货物后，立即送往{put_goods_id}",
    "先去{get_pos_id}取货，之后请送到{put_goods_id}",
    "我需要你到{get_pos_id}取货，接着把货物送到{put_goods_id}",
    "请执行从{get_pos_id}取货并运送到{put_goods_id}的任务",
    "请在{get_pos_id}取货后，前往{put_goods_id}完成送货",
    "请在{get_pos_id}取货，然后直接送到{put_goods_id}",
    "请前往{get_pos_id}领取货物，并将其送至{put_goods_id}",
    "请在{get_pos_id}取货后，再在{put_goods_id}放货，搬运方案为{transport_plan_id}。",
    "从{get_pos_id}取货，然后放到{put_goods_id}，搬运方案为{transport_plan_id}。",
    "请在{get_pos_id}取货，随后在{put_goods_id}放货，使用{transport_plan_id}搬运方案。",
    "在{get_pos_id}取货后，将货物运送至{put_goods_id}放货。",
    "从{get_pos_id}获取货物，然后放到{put_goods_id}，按照搬运方案{transport_plan_id}进行。",
    "请在{get_pos_id}取货后，放到{put_goods_id}。",
    "在{get_pos_id}取完货后，请放到{put_goods_id}，按照{transport_plan_id}搬运方案执行。",
    "请从{get_pos_id}获取货物，然后放到{put_goods_id}。",
    "从{get_pos_id}取货，然后放到{put_goods_id}，使用搬运方案{transport_plan_id}。",

    "请先到取货点领取货物，接着将它们送至{put_goods_id}。",
    "请先到{get_pos_id}取货，之后请将货物送至指定的放货地点。",
    "请前往指定地点取货，并随后将货物送至{put_goods_id}。",
    "请先领取货物，然后将其运送到{put_goods_id}。",
    "请先到{get_pos_id}取货，然后请将货物送至交货点。",
    "请先到取货点领取货物，随后请将货物送至{put_goods_id}。",
    "请前往{get_pos_id}领取物品，然后将其送至交货地点。",
    "请先到指定地点取货，然后将其送至{put_goods_id}。",

    "请先到取货点取货物，然后送往放货点。",
    "请前往指定地点取货，并随后将货物送达目的地。",
    "请先领取货物，接着将其运送到指定的放货地址。",
    "请先到取货点取货，之后请将货物送至指定位置。",
    "请先到指定地点领取货物，随后将货物送达放货库位。",
    "请先领取货物，随后请将货物送达放货地点。",

]


get_put_info = [
    "请先到{get_pos_id}取货，随后将货物送至{put_goods_id}",
    "请在{get_pos_id}取完货物后，立即送往{put_goods_id}",
    "先去{get_pos_id}取货，之后请送到{put_goods_id}",
    "我需要你到{get_pos_id}取货，接着把货物送到{put_goods_id}",
    "请执行从{get_pos_id}取货并运送到{put_goods_id}的任务",
    "请在{get_pos_id}取货后，前往{put_goods_id}完成送货",
    "请在{get_pos_id}取货，然后直接送到{put_goods_id}",
    "请前往{get_pos_id}领取货物，并将其送至{put_goods_id}",
    "请在{get_pos_id}取货后，再在{put_goods_id}放货，搬运方案为{transport_plan_id}。",
    "从{get_pos_id}取货，然后放到{put_goods_id}，搬运方案为{transport_plan_id}。",
    "请在{get_pos_id}取货，随后在{put_goods_id}放货，使用{transport_plan_id}搬运方案。",
    "在{get_pos_id}取货后，将货物运送至{put_goods_id}放货。",
    "从{get_pos_id}获取货物，然后放到{put_goods_id}，按照搬运方案{transport_plan_id}进行。",
    "请在{get_pos_id}取货后，放到{put_goods_id}。",
    "在{get_pos_id}取完货后，请放到{put_goods_id}，按照{transport_plan_id}搬运方案执行。",
    "请从{get_pos_id}获取货物，然后放到{put_goods_id}。",
    "请在{get_pos_id}获取货物，然后放到{put_goods_id}，按照{transport_plan_id}搬运方案进行。",
    "从{get_pos_id}取货，然后放到{put_goods_id}，使用搬运方案{transport_plan_id}。",
]

get_put_info_en = [
    "First, go to {get_pos_id} to pick up the cargo, then deliver them to {put_goods_id}.",
    "Proceed to {get_pos_id} to pick up the pallet, afterward transport the pallet to {put_goods_id}.",
    "Begin by moving to {get_pos_id} to pick up the load, subsequently ship the load to {put_goods_id}.",
    "Start at {get_pos_id} to get the cargo, following this, transport the cargo to {put_goods_id}.",
    "Firstly, navigate to {get_pos_id} to obtain the load, then route the load to {put_goods_id}.",
    "Commence at {get_pos_id} to get goods, post this, direct the shipment to {put_goods_id}.",
    "Make your way to {get_pos_id} to get the goods, after that, channel the goods to {put_goods_id}.",
    "Head to {get_pos_id} initially to pick up the load, subsequently steer the consignment to {put_goods_id}.",
    
    "After picking up load at {get_pos_id}, transport the load to {put_goods_id} for unloading.",
    "Once you've picked up the cargo at {get_pos_id}, ship it to {put_goods_id} for offloading.",
    "Following the get goods at {get_pos_id}, deliver the goods to {put_goods_id} for putting.",
    "Upon acquiring the cargo at {get_pos_id}, ship the cargo to {put_goods_id} for placement.",
    "After picking up the load at {get_pos_id}, channel the shipment to {put_goods_id} for unloading.",
]

ack_get_put_id_info = [
	"请提供您的取货和放货的具体位置。",
	"请告知我您的取货点和放货点的详细信息。",
	"请明确指出您的取货位置和放货位置。",
	"请告诉我您的取货点和放货点。",
	"请指出您需要取货和放货的地点。",
	"请向我提供取货和放货的地点信息。",
	"请说明您的取货地点与放货地点。",
	"请告知我您计划取货和放货的地点。",
]

ask_get_put_id_info_en = [
      "Please provide the specific locations for your goods pickup and placement.",
      "Kindly furnish the precise sites for pickup and unload of your cargo.",
      "Please indicate the detailed locations for the getting and putting of your goods.",
      "Would you supply the particular places for obtaining and releasing your load?",
      "Share the exact location for the pickup and put of your cargo.",
      "Please detail the accurate area for your cargo pickup and unload.",
      "Could you disclose the specific areas for the pickup and delivery of your load?",
]

ans_get_put_id_info = [
    "您的取货位置是{get_pos_id}，而放货位置则是{put_goods_id}。",
    "{get_pos_id}作为取货点，{put_goods_id}作为放货点。",
    "货物的提取地点为{get_pos_id}，而放货地点为{put_goods_id}。",
    "取货的指定点是{get_pos_id}，放货的指定点是{put_goods_id}。",
    "货物领取点为{get_pos_id}，而货物放置点为{put_goods_id}。",
    "您的取货地点是{get_pos_id}，放货地点是{put_goods_id}。",
]

ans_get_put_id_info_en = [
    "Your cargo collection site is {get_pos_id}, and the delivery location is {put_goods_id}.",
    "The pickup spot for your goods is {get_pos_id}, whereas the drop-off point is {put_goods_id}.",
    "The location for obtaining your load is {get_pos_id}, and the placement site is {put_goods_id}.",
    "Your cargo pickup position is {get_pos_id}, and the destination for unloading is {put_goods_id}.",
    "The spot to collect your goods is {get_pos_id}, while the put location is {put_goods_id}.",
    "The place for getting your cargo is {get_pos_id}, and the spot for putting is {put_goods_id}.",
    "The area for your goods pickup is {get_pos_id}, and the destination for placing is {put_goods_id}.",
    "The location to pickup cargo is {get_pos_id}, and the offload destination is {put_goods_id}.",
    "The site for getting your load is {get_pos_id}, and the unloading site is {put_goods_id}.",
]

################################################# 9. task process template info #######################################################
task_process_run_info = [
    "请启动任务流程[{task_process_id}]",
    "开始执行任务流程[{task_process_id}]",
    "请运行任务流程[{task_process_id}]",
    "我需要执行任务流程[{task_process_id}]",
    "请进行任务流程[{task_process_id}]操作",
    "请按照任务流程[{task_process_id}]执行",
    "请按照流程[{task_process_id}]进行任务",
    "请执行名为[{task_process_id}]的任务流程",

    "请按照流程[{task_process_id}]进行任务，重复{num}次。",
    "请开始流程[{task_process_id}]的任务，重复执行{num}次。",
    "请按照流程[{task_process_id}]进行任务，搬运方案为{transport_plan_id}。",
    "启动流程[{task_process_id}]的任务序列，搬运方案为{transport_plan_id}，重复执行{num}次。",
    "按照流程[{task_process_id}]进行任务，搬运方案为{transport_plan_id}，无需重复。",
    "请开始执行流程[{task_process_id}]的任务，搬运方案为{transport_plan_id}，重复执行{num}次。",
    "执行流程[{task_process_id}]的任务，搬运方案为{transport_plan_id}。",
]

task_process_run_info_en = [
    "Please run the tasklist [{task_process_id}].",
    "Kindly execute the task procedure [{task_process_id}].",
    "Could you begin the workflow [{task_process_id}]?",
    "Please activate the tasklist [{task_process_id}].",
    "Execute the commencement of the taskflow [{task_process_id}].",
    "Carry out the operation of the tasklist [{task_process_id}].",
    "Engage the activation of the workflow [{task_process_id}].",
    
    "Please carry out the task process titled [{task_process_id}].",
    "Execute the workflow named [{task_process_id}], please.",
    "Kindly perform the procedure known as [{task_process_id}].",
    "Activate the task cycle named [{task_process_id}], please.",
    
    "Please follow the procedure [{task_process_id}] to execute the task, repeating it {num} times.",
    "Carry out the mission according to the tasklist [{task_process_id}], performing it {num} times.",
    "Please implement the task based on the workflow [{task_process_id}], iterating {num} times.",
    "Start the workflow defined by [{task_process_id}], repeating {num} times in sequence.",
    "Launch the tasklist outlined in [{task_process_id}], conducting it {num} times.",
    "activate the task procedure of [{task_process_id}], performing them {num} times.",

    "Perform task [{task_process_id}] for {num} amount of times.",
    "Execute task [{task_process_id}] for {num} repetitions.",
    "Complete task [{task_process_id}] {num} number of times.",
    "Repeat task [{task_process_id}] {num} times.",
    "Carry out task [{task_process_id}] {num} times.",
    "Do task [{task_process_id}] for {num} cycles.",
    "Perform task [{task_process_id}] {num} times.",
    "Run {num} cycles of task [{task_process_id}].",
    "Loop task [{task_process_id}] {num} times.",
    "Repeat action [{task_process_id}] for {num} intervals.",
    "Perform task [{task_process_id}] for {num} cycles.",
    "Execute task [{task_process_id}] for {num} rounds.",
    "Do task [{task_process_id}] for {num} intervals.",
    "Repeat task [{task_process_id}] for {num} times.",
    "Carry out task [{task_process_id}] for {num} loops.",
    "Complete task [{task_process_id}] for {num} repetitions.",
    "Run task [{task_process_id}] for {num} cycles.",
    "Repeat action [{task_process_id}] for {num} rounds.",
    "Perform task [{task_process_id}] for {num} repetitions in total.",
    "Loop task [{task_process_id}] for {num} rounds.",

    "Run task [{task_process_id}].",
    "Perform task [{task_process_id}].",
    "Execute task [{task_process_id}].",
    "Carry out task [{task_process_id}].",
    "Do task [{task_process_id}].",
    "Repeat task [{task_process_id}].",
    "Run action [{task_process_id}].",
    "Execute task [{task_process_id}] once.",
    "Do task [{task_process_id}] now.",
    "Carry out task [{task_process_id}] immediately.",
    "Repeat task [{task_process_id}].",
    "Perform task [{task_process_id}].",
    "Run task [{task_process_id}].",
    "Carry out task [{task_process_id}] continuously.",


]

process_name = [
    "取货111",
    "放货222",
    "充电1",
    "移动abc",
    "取货test",
    "放货345",
    "先取货再放货",
    "执行任务1",
    "操作222",
    "流程abc",
    "先取货再放货",
    "test",
    "123321",
]

process_name_en = [
    "取货_送至B点#1",
    "命令模式_任务A",
    "自然语言#取货",
    "查询状态_车体",
    "流程控制_充电",
    "复合任务_取放$1",
    "get序列01",
    "put取货#002",
    "task进程III",
    "test#4A",
    "StatusQuery_03#",
    "CmdModeControl_07",
    "hello取货#09",
    "charge序列X",
    "workflow_流程08",
    "VoiceOp_任务五",
    "test",
    "PASS",
]

################################################# 10. gen task template info #######################################################
gen_task_info = [
    "请为我创建前往{get_pos_id}执行取货的任务。",
    "帮我生成一个到{get_pos_id}取货的指令。",
    "请生成任务：前往{get_pos_id}并取货。",
    "需要创建一个去{get_pos_id}取货的流程。",
    "请构建并生成去{get_pos_id}取货的作业指令。",

    "请帮我创建一个任务，前往{put_goods_id}放货。",
    "为我生成去{put_goods_id}放置货物的任务流程。",
    "需要生成一个到{put_goods_id}放货的操作指令。",
    "请创建并生成前往{put_goods_id}进行货物放置的任务。",
    "帮我构建一个任务，内容是去{put_goods_id}完成放货工作。",

    "请创建一个任务，前往{charge_pos_id}进行充电。",
    "为我生成一个指令，以便去{charge_pos_id}充电。",
    "帮我生成一个充电任务，指定位置为{charge_pos_id}。",
    "请生成并创建一个到{charge_pos_id}的充电任务。",
    "需要生成一个任务，目标是去{charge_pos_id}充电。",

    # "请创建一个任务，包括前往{get_pos_id}取货和去{put_goods_id}放货。",
    # "帮我生成一个流程，先到{get_pos_id}取货，然后去{put_goods_id}放货。",
    # "请生成任务：首先是去{get_pos_id}取货，接着去{put_goods_id}放货。",
    # "为我创建一个指令，涉及去{get_pos_id}取货和去{put_goods_id}放货。",
    # "请生成一个包含取货和放货的复合任务，去{get_pos_id}取货后去{put_goods_id}放货。",
]


ans_gen_task_info = [
    "任务正在创建中。您需要再添加其他任务吗？",
    "好的，任务已开始生成。是否还需要生成更多的任务？",
    "正在为您生成任务，请告诉我是否需要继续添加其他任务。",
    "任务生成中，您是否希望继续创建额外的任务？",
    "已启动任务生成。请问您是否还需要生成其他任务？",
]

ask_to_run_generated_task = [
	"开始执行创建的任务。",
	"立刻开始执行。",
	"启动执行流程。",
	"开始执行这些任务。",
	"着手执行。",
]

################################################# 11. cmd control template info #######################################################


pause_info = [
    "请暂停当前任务",
    "车辆暂停运行",
    "请中断车辆操作",
    "让车辆暂停所有活动",
    "暂停",
    "车辆暂停",
    "请暂停",
]

pause_info_en = [
    "Please put the current task on hold.",
    "Would you suspend the current operation?",
    "Please place the mission on pause.",
    "Would you pause the current task?",
    "The AGV pauses its active operation.",
    "Interrupt the process.",
    "Pause the execution.",
    "pause",
    "pause, please?",
    "Pause the task.",
    "Pause the operation.",
    "Pause everything.",
    "Pause the process.",
    "Pause the current task.",
    "Pause the current operation.",
    "Pause all tasks.",
    "Pause all operations.",
    "Pause all activities.",
    "Pause the ongoing task.",
    "Pause the ongoing operation.",
    "Pause the job.",
    "Pause what you're doing.",
    "Pause the activity.",

    "Hold the task.",
    "Hold the operation.",
    "Hold everything.",
    "Hold the process.",
    "Hold the current task.",
    "Hold the current operation.",
    "Hold all tasks.",
    "Hold all operations.",
    "Hold all activities.",
    "Hold the ongoing task.",
    "Hold the ongoing operation.",
    "Hold the job.",
    "Hold what you're doing.",
    "Hold the activity.",

    "Suspend the task.",
    "Suspend the operation.",
    "Suspend everything.",
    "Suspend the process.",
    "Suspend the current task.",
    "Suspend the current operation.",
    "Suspend all tasks.",
    "Suspend all operations.",
    "Suspend all activities.",
    "Suspend the ongoing task.",
    "Suspend the ongoing operation.",
    "Suspend the job.",
    "Suspend what you're doing.",
    "Suspend the activity.",

    "Temporarily pause the task.",
    "Temporarily pause the operation.",
    "Pause and hold the task.",
    "Pause and hold the operation.",
    "Pause and suspend the activity.",
    "Halt the task.",
    "Halt the operation.",
    "Halt all activities.",
    "Halt the process.",
    "Halt everything",
]

stop_info = [
    "请立即停车",
    "车辆需要停下",
    "请让车辆停下来",
    "停车",
    "停止所有车辆任务",
    "车辆需要立刻停止",
    "停止",
]

stop_info_en = [
    "stop the forklift right now?",
    "forklift need to stop",
    "stop",
    "put an end to current task.",
    "terminate aAGV's missions.",

    "Stop the task temporarily.",
    "Stop the operation temporarily.",
    "Stop the current task.",
    "Terminate the task.",
    "Abort the task.",
    "Stop the task.",
    "End the task.",
    "Shut down the task.",
    "Cease the task.",
    "Discontinue the task.",
    "Quit the task.",
    "Abort the operation.",
    "Terminate the operation.",
    "End the operation.",
    "Stop the operation.",
    "Shut down the operation.",
    "Cease the operation.",
    "Discontinue the operation.",
    "Quit the operation",
    "Abort what you're doing.",
    "Terminate what you're doing.",
    "End what you're doing.",
    "Quit what you're doing.",
    "Abort all tasks.",
    "Terminate all tasks.",
    "End all tasks.",
    "Stop all tasks.",
    "Cease all tasks.",
    "Abort everything.",
    "Terminate everything.",
    "End everything.",
    "Stop everything.",
    "Cease everything",
    "Terminate the current task.",
    "Abort the current task.",
    "End the current task.",
    "Stop the current task.",
    "Shut down the current",
    "Abort the ongoing task.",
    "Terminate the ongoing task.",
    "End the ongoing task.",
    "Stop the ongoing task",
]

continue_info = [
    "请继续执行任务",
    "解除暂停，继续任务流程",
    "请让车辆继续运行",
    "继续车辆的当前任务",
    "继续",
    "请重新开始",
]

continue_info_en = [
    "Please proceed with the mission.",
    "Kindly resume the operation.",
    "Lift the hold and proceed with the task process.",
    "Cancel the pause and continue with the mission.",
    "Terminate the suspension and carry on with the task.",
    "continue",
    "Please resume the task.",

    "Continue the task.",
    "Carry on with the task.",
    "Keep going.",
    "Pick up where you left off.",
    "Start again from where you paused.",
    "Keep running the task.",
    "Proceed with the task.",
    "Resume what you were doing.",
    "Restart the operation.",
    "Continue the task.",
    "Resume the task.",
    "Keep going.",
    "Carry on with the task.",
    "Resume the operation.",
    "Unpause the task.",
    "Restart the task.",
    "Restart from where you stopped.",
    "Reboot the task.",
    "Resume the process.",
    "Keep working on it.",
    "Go back to the task.",
    "Get back to the job.",
    "Unfreeze the task.",
    "Reactivate the task.",
    "Resume operations.",
    "Start the task again.",
    "Restart the activity.",
    "Get back to the task.",
    "Pick up the activity.",
    "Carry on from where you paused.",
    "Keep moving with the operation.",
    "Start from where you stopped.",
    "Continue the operation.",
    "Reactivate operations.",
    "Unpause and continue.",
    "Reinitiate the task.",
    "Resume the activity.",
    "Get back to the operation.",
    "Restart operations.",
    "Start where you left off.",
    "Restart where you paused.",
    "Go back to the process.",
    "Carry on working on it.",
    "Unpause the operation.",
    "Resume task",
    "Resume",
    "Get back to work.",
    "Reboot the current task.",
    "Pick up the current activity.",
    "Start the task again from pause.",
    "Reactivate the process.",

]

reset_info = [
    "请将车辆恢复到初始状态。",
    "请重置车辆设置。",
    "请初始化车辆。",
    "请执行车辆的复位操作。",
    "请对车辆进行系统重置。",
    "复位车辆",
    "初始化车辆",
    "执行车辆初始化操作",
]

reset_info_en = [
    "Please revert the AGV to its initial condition.",
    "Could you reset the forklift to its factory settings?",
    "reset",
    "Would you reset the vehicle to its primary state?",
    "Please reset the AGV's configuration.",
    "Could you restore the car's initial settings?",
    "Would you initiate the forklift's default parameters?",
    "Can you reconfigure the vehicle to its original state?",
    "please initialize forklift's settings",
    "reset AGV",
    "Perform AGV initialization operation",
]

cancel_info = [
    "请清空所有待执行的任务",
    "取消所有的任务",
    "请立即清空车辆的所有任务",
    "我要取消所有的任务",
    "清空任务列表",
    "执行清空操作",
]

cancel_info_en = [
    "Please erase all tasks.",
    "Could you clear all upcoming duties?",
    "Would you delete all scheduled tasks?",
    "Please remove all queued operations.",
    "I want to delete all tasks",
    "Cancel all missions.",
    "clear tasklist",
    "perform clear operations",
    "Cancel the task.",
    "Cancel the operation.",
    "Cancel what you're doing.",
    "Cancel all tasks.",
    "Cancel everything.",
    "Cancel the current task.",
    "Cancel the ongoing task.",
]


cmd_control_info = [
    {"pause": pause_info},
    {"stop": stop_info},
    {"continue": continue_info},
    {"reset": reset_info},
    {"cancel": cancel_info},
]

cmd_control_info_en = [
    {"pause": pause_info_en},
    {"stop": stop_info_en},
    {"continue": continue_info_en},
    {"reset": reset_info_en},
    {"cancel": cancel_info_en},
]

cmd_control_map_zh = [
    {"pause": "暂停"},
    {"stop": "停止"},
    {"continue": "继续"},
    {"reset": "复位"},
    {"cancel": "取消"},
]


######################################################### mix order info ################################################################################
ask_mix_order_info = [
    "请先去{charge_pos_id}充电，接着去{get_pos_id}取货，然后放货到{put_goods_id}位置，紧随执行{num}次[{task_process_id}]任务流程，最后执行车辆{control_type}任务。",
    "请执行{num}次[{task_process_id}]任务流程，接着去{charge_pos_id}充电，最后执行车辆{control_type}任务。",
    "请先去{charge_pos_id}充电，接着去{get_pos_id}取货，紧随执行{num}次[{task_process_id}]任务流程，然后放货到{put_goods_id}位置，最后执行车辆{control_type}任务。",
    "请先去{get_pos_id}取货，然后去{charge_pos_id}充电，接着放货到{put_goods_id}位置。",
    "请先去{get_pos_id}取货，然后放货到{put_goods_id}位置，紧随执行{num}次[{task_process_id}]任务流程。",
    "请先去{charge_pos_id}充电，接着去{get_pos_id}取货，然后放货到{put_goods_id}位置。",
    "执行{num}次[{task_process_id}]任务流程，最后执行车辆{control_type}任务。",
    "请先去执行{num}次[{task_process_id}]任务流程，然后去{charge_pos_id}充电，最后执行车辆{control_type}任务。",
    "请先车辆{control_type}，然后去{charge_pos_id}充电，接着去执行{num}次[{task_process_id}]任务流程。",
    "请先车辆{control_type}，接着去{get_pos_id}取货，然后放货到{put_goods_id}位置。",
    "先进行车辆{control_type}操作，去执行{num}次[{task_process_id}]任务流程。",
    "先进行车辆{control_type}操作，去执行去{charge_pos_id}充电任务。",
    
    #"请前往{charge_pos_id}进行电池充电，随后上报AGV状态{special_query}，然后去{get_pos_id}提取货物，再将物品放置于{put_goods_id}。",
    #"帮我查看车体状态{special_query}，接着去{get_pos_id}领取货物，然后到{put_goods_id}放置货物，紧随进行{num}次[{task_process_id}]任务流程。",
    #"请在{charge_pos_id}进行电力补给，然后查询AGV状态{special_query}，之后去{get_pos_id}获取货物，再将货物运输到{put_goods_id}，继而执行{num}次[{task_process_id}]流程，最终执行车辆{control_type}任务。",
    #"先执行车辆{control_type}任务，接着去{charge_pos_id}充电，紧随执行紧随执行{num}次[{task_process_id}]操作流程；跟着先去{get_pos_id}获取货物，再将货物放置到{put_goods_id}，最后查询AGV车体状{special_query}",

]

ask_mix_order_info_en = [
  "First, proceed to {charge_pos_id} for charging, then head to {get_pos_id} for pickup cargo, subsequently deliver to {put_goods_id}, followed by performing {num} rounds of [{task_process_id}] task procedure, and conclude with the {control_type} AGV operation",
  "Carry out the [{task_process_id}] tasklist {num} times, then proceed to {charge_pos_id} for charging forklift, and finally perform the {control_type} operation.",
  "First, head to {charge_pos_id} for charging forklift, then proceed to {get_pos_id} for pickup load, next carry out {num} times [{task_process_id}] task procedure, subsequently deliver load to {put_goods_id} location, and finally perform the {control_type} control operation.",
  "Initiate at {get_pos_id} location for getting goods, subsequently go to {charge_pos_id} charge parks to supplement electricity, and then transfer the cargo to the designated {put_goods_id} spot.",
  "First, head to {get_pos_id} to pick up cargo, then put to {put_goods_id} location, and immediately perform the [{task_process_id}] task procedure {num} times.",
  "navigate to {charge_pos_id} storage location for charging, then proceed to {get_pos_id} for getting pallet, and finally deliver the pallet at {put_goods_id} location.",
  "Perform the [{task_process_id}] workflow {num} times, then run the {control_type} control order.",
  "conduct the [{task_process_id}] tasklist {num} times, then proceed to {charge_pos_id} charge spot for charging, and ultimately perform the {control_type} control operation.",
  "perform the {control_type} control operation for AGV; next, head to {charge_pos_id} to charge forklift, and then execute the [{task_process_id}] workflow {num} times",
  "Execute the {control_type} control instruction on forklift, next, move to {get_pos_id} for acquiring the cargo, and then deliver the cargo to the {put_goods_id} position.",
  "Start with the {control_type} control operation, and subsequently execute the [{task_process_id}] tasklist {num} times.",
  "Start with the {control_type} control command for the AGV, and subsequently undertake the charging operation at {charge_pos_id} location.",

]

