# -*- coding: utf-8 -*-
import json
import os
import re
class analysisCfg():
    def __init__(self,platform,taskID,userID):
        self.platform = platform
        self.taskID =taskID
        self.userID = userID

        self.render_mode = ''

        # delfix = re.findall('^\d?\D', taskID)
        # if delfix:
        #     taskID = taskID.replace(delfix[0], '')
        self.taskID = re.sub('^\d?\D','',taskID)

        self.k_jsonerror = False

        self.platform_address = {'c_W2rb':r'\\10.60.100.101','c_W3rb':r'\\10.30.100.102',\
                            'c_W4rb':r'\\10.40.100.101','c_W9rb':r'\\10.80.100.101',\
                            'c_GPUrb':r'\\10.90.100.101'}

        # cfg_jsonPath = r'D:\Work\cfg\cfg\task.json'
        # sys_jsonPath = r'D:\Work\cfg\sys_cfg\system.json'
        #
        # self.k_cfg_json = json.loads(open(cfg_jsonPath).read())
        # self.k_sys_json = json.loads(open(sys_jsonPath).read())


        self.userID_up =''
        try:
            if int(userID[-3:]) >= 500:
                self.userID_up = str(int(userID) - int(userID[-3:]) + 500)
            else:
                self.userID_up = str(int(userID) - int(userID[-3:]))
        except Exception as e:
            print (e)

        #客户端
        #// 10.60.100.101 / d / ninputdata5 / 10572267 / temp\server.cfg
        #\\10.60.100.101\p5\temp\10572267_render\cfg

        #网页端
        #\\10.60.100.101\p5\config\1163000\1163153\10583609
        #\\10.60.100.101\p5\temp\10583609_render\cfg

        #py_cfg_Path = os.path.join(platform_address[platform],'p5','temp','%s_render','cfg' %taskID)
        #web_cfg_Path = os.path.join(platform_address[platform],'p5','config',self.userID_up,self.userID,self.taskID)

        #py_cfg_Path = r'D:\Work\china_client\cfg'
        py_cfg_Path = r'D:\Work\china_web\cfg'
        web_cfg_Path = r'D:\Work\china_web\10583609'

        py_cfg_p      = os.path.join(py_cfg_Path,'py.cfg')
        #客户端配置文件路径
        plugins_cfg_p = os.path.join(py_cfg_Path,'plugins.cfg')
        server_cfg_p  = os.path.join(py_cfg_Path,'server.cfg')
        #网页端配置文件路径
        web_plugins_json_p = os.path.join(web_cfg_Path,'plugins.json')
        web_render_json_p = os.path.join(web_cfg_Path, 'render.json')

        if os.path.exists(py_cfg_p) and os.path.exists(plugins_cfg_p) and os.path.exists(server_cfg_p):
            #客户端
            self.render_mode = 'client'
            # 读取配置文件
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


        elif os.path.exists(py_cfg_p) and os.path.exists(web_plugins_json_p) and os.path.exists(web_render_json_p):
            #网页端
            self.render_mode = 'web'
            #读取配置文件
            self.plugins_info = json.loads(open(web_plugins_json_p).read())
            self.web_render_info  = json.loads(open(web_render_json_p).read())

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


        self.function_path = os.path.join(self.platform_address[platform],'o5','py','model','function')




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
        k_path = self.analysisPath()

        k_mapping = {}
        #客户端
        if self.render_mode == 'client':
            if 'mounts' in self.server_info:
                for key_diver in self.server_info['mounts']:
                    kexp = r'^(\w:)'
                    #匹配字母开头
                    if re.findall(kexp,str(key_diver)):
                        netpath = os.path.join(self.storage_path,self.server_info['mounts'][key_diver])
                        netdict = {key_diver:os.path.normpath(netpath)}
                        k_mapping.update(netdict)

            B_plugin_path = {'B:':self.B_plugin_path}
            k_mapping.update(B_plugin_path)

        #网页端
        elif self.render_mode == 'web':
            if 'mntMap' in self.web_render_info:
                for key_diver in self.web_render_info['mntMap']:
                    kexp = r'^(\w:)'
                    if re.findall(kexp, str(key_diver)):
                        netpath = os.path.normpath(self.web_render_info['mntMap'][key_diver])
                        netdict = {key_diver:netpath}
                        k_mapping.update(netdict)

        print(k_mapping)
        return k_mapping

    def analysisPath(self):


        # B盘插件路径
        self.B_plugin_path = ''
        if 'PLUGINPATH' in self.py_info:
            self.B_plugin_path = os.path.normpath(eval(self.py_info['PLUGINPATH']))
        elif 'PLUGINPATHLIST' in self.py_info:
            B_plugin_paths = eval(self.py_info['PLUGINPATHLIST'])
            self.B_plugin_path = os.path.normpath(B_plugin_paths[0])
        else:
            print('B plugins path error ----!!!!')

        # RayvisionCustomConfig 路径
        customfile_Path = os.path.join(self.B_plugin_path, 'custom_config', self.userID)
        # prerender路径
        C_prerender_path = os.path.join(self.platform_address[self.platform], 'o5', 'py', 'model', 'user', self.userID)


        print('1111')
        if self.render_mode == 'client':

            #图片输出路径
            k_user_outputPath = eval(self.py_info['G_PATH_USER_OUTPUT'])

            #客户的存储路径
            k_input_proj = eval(self.py_info['G_PATH_INPUTPROJECT'])
            #获取存储路径 d\inputdata5
            self.storage_path = ''
            if self.userID_up in k_input_proj and self.userID in k_input_proj:
                self.storage_path = os.path.normpath(k_input_proj.split(self.userID_up)[0])
            else: print('Get storage path error ----!!!!')

            k_input_file = eval(self.py_info['G_PATH_INPUTFILE'])


            #组合出 input的 maya文件路径
            k_filePath = os.path.normpath(os.path.dirname(k_input_file))
            k_exp = r"^\w(:)"
            if re.findall(k_exp,k_filePath):
                g_input_file = re.sub(k_exp,k_filePath[0],k_filePath)
                k_input_filePath = os.path.join(k_input_proj,g_input_file)

        elif self.render_mode == 'web':
            print('222')
            #获取 k_input_filePath
            if 'common' in self.web_render_info:
                if 'inputCgFile' in self.web_render_info['common']:
                    k_input_file = self.web_render_info['common']['inputCgFile']
                    k_input_filePath = os.path.dirname(k_input_file)
                    print(k_input_filePath)
                else:print('Get input file path error ----!!!!')
            print('3333')
            #获取k_user_outputPath
            if 'common' in self.web_render_info:
                if 'userOutputPath' in self.web_render_info['common']:
                    k_output_file = self.web_render_info['common']['userOutputPath']
                    k_user_outputPath = os.path.dirname(k_output_file)
                    print(k_user_outputPath)
                else:print('Get output file path error ----!!!!')


        return (k_input_filePath,k_user_outputPath,customfile_Path,C_prerender_path,self.B_plugin_path)


if __name__ == '__main__':
    a=analysisCfg('c_W2rb','111','1863567')
    a.analysisMapping()
