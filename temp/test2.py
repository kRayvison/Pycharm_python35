a=r'\\10.60.200.103\d\inpudata5'
b=r'1859500/1859970/'
import os
import re


a={'1925000/1925024/Y': 'Q','1925000/1925024/B': 'B'}

A={'taskOverTime': '12', 'pernodeframesenable': '0', 'render_file': 'I:/bingma/yancao.rayvision', 'cgv': 'maya2015', 'usedRenderer': 'mentalRay', 'kg': '32', 'afterFirstRender': 'fullSpeed', 'submit_mode': '2', 'cgFile': 'I:/bingma/yancao.mb', 'output': 'None', 'dependency': '0', 'renderer': 'mentalRay', 'sceneFile': 'I:/bingma/yancao.rayvision', 'renderableCamera': 'persp1Shape', 'batchPrior': '', 'zone': '1', 'height': '1080', 'projectId': '106955', 'name': '', 'create_folder': '[]', 'munu_pyd_time': 'Sat Sep 01 20:58:18 2018', 'taskId': '10572267', 'firstFrames': '', 'project': 'maya', 'memorySize': '64', 'allLayer': 'defaultRenderLayer', 'projectSymbol': 'lanmu', 'path1': 'I:/bingma/xizhichangle.jpg>>/1863500/1863567/I/bingma/xizhichangle.jpg', 'cgSoftName': 'maya', 'allCamera': 'frontShape,persp1Shape,perspShape,sideShape,topShape', 'frames': '1-70[1]', 'renderableLayer': 'defaultRenderLayer', 'tiles': '1', 'mountFrom': "{'/1863500/1863567/I': 'I:'}", 'original_cg_file': 'I:/bingma/yancao.mb', 'sceneProject': 'None', 'pernodeframes': '', 'project_id': '106955', 'width': '1920', 'level': 'None'}

print(A['mountFrom'])

B=eval(A['mountFrom'])


for key_diver,value in B.items():
    print(key_diver,value)
#print('netpath =%s' %A)