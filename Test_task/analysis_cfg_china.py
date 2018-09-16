# -*- coding: utf-8 -*-
import json
import os
import re
class analysisCfg():
    def __init__(self,platform,taskID,userID):

        delfix = re.findall('^\d?\D', taskID)
        if delfix:
            taskID = taskID.replace(delfix[0], '')


        self.k_jsonerror = False

        platform_address = {'c_W2rb':r'\\10.60.100.101','c_W3rb':r'\\10.30.100.102',\
                            'c_W4rb':r'\\10.40.100.101','c_W9rb':r'\\10.80.100.101',\
                            'c_GPUrb':r'\\10.90.100.101'}

        # cfg_jsonPath = r'D:\Work\cfg\cfg\task.json'
        # sys_jsonPath = r'D:\Work\cfg\sys_cfg\system.json'
        #
        # self.k_cfg_json = json.loads(open(cfg_jsonPath).read())
        # self.k_sys_json = json.loads(open(sys_jsonPath).read())


        userID_up =''

        if int(userID[-3:]) >= 500:
            userID_up = str(int(userID) - int(userID[-3:]) + 500)
        else:
            userID_up = str(int(userID) - int(userID[-3:]))

        #cfgPath = os.path.join(platform_address[platform],'p5','temp','%s_render','cfg' %taskID)


        cfgPath = r'D:\Work\china_cfg'


        py_cfg_p      = os.path.join(cfgPath,'py.cfg')
        plugins_cfg_p = os.path.join(cfgPath,'plugins.cfg')
        server_cfg_p  = os.path.join(cfgPath,'server.cfg')

        print(cfgPath)

        if os.path.exists(py_cfg_p) and os.path.exists(plugins_cfg_p) and os.path.exists(server_cfg_p):

            self.server_info  = eval(open(server_cfg_p).read())

            self.plugins_info = eval(open(plugins_cfg_p).read())


            result = {}
            with open(py_cfg_p,"r") as f:
                while 1:
                    line = f.readline()
                    if "=" in line:
                        line_split = line.split("=")
                        result[line_split[0].strip()] = line_split[1].strip()
                    else:
                        break
                self.py_info = result

        else:self.k_jsonerror = True


        self.function_path = os.path.join(platform_address[platform],'o5','py','model','function')

        self.C_prerender_path = os.path.join(platform_address[platform], 'o5', 'py', 'model', 'user',userID)




    def analysisPlugins(self):
        k_plugins = {}
        k_plugins = (self.plugins_info['plugins'] if self.plugins_info['plugins'] else '')
        return k_plugins

    def analysisSoft(self):
        k_mayaver = ''
        if self.plugins_info['renderSoftware'] == 'Maya':
            k_mayaver = self.plugins_info['softwareVer']
        else : k_mayaver = 'It is not maya task!!!'
        return k_mayaver

    def analysisMapping(self):
        k_mapping = {}
        k_mapping = (self.k_cfg_json['mnt_map'] if self.k_cfg_json['mnt_map'] else '')
        #B盘路径

        if 'plugin_path' in self.k_sys_json['system_info']['common']:
            k_Bpath = self.k_sys_json['system_info']['common']['plugin_path']
        elif 'plugin_path_list' in self.k_sys_json['system_info']['common']:
            k_Bpath = self.k_sys_json['system_info']['common']['plugin_path_list'][0]

        k_pluginPath = {'B:':k_Bpath}
        k_mapping.update(k_pluginPath)
        return k_mapping

    def analysisPath(self):
        k_path = {}
        k_input_proj = eval(self.py_info['G_PATH_INPUTPROJECT'])
        k_input_file = eval(self.py_info['G_PATH_INPUTFILE'])
        k_user_outputPath = eval(self.py_info['G_PATH_USER_OUTPUT'])
        k_filePath = os.path.normpath(os.path.dirname(k_input_file))

        k_exp = r"^\w(:)"
        if re.findall(k_exp,k_filePath):
            g_input_file = re.sub(k_exp,k_filePath[0],k_filePath)
            k_input_filePath = os.path.join(k_input_proj,g_input_file)
        #k_input_proj = os.path.normpath(k_input_proj)
        #return (k_input_proj,k_input_file,g_input_file,k_input_filePath)

        return (k_input_filePath,k_user_outputPath)


if __name__ == '__main__':
    a=analysisCfg()
    print (a.analysisMnt())