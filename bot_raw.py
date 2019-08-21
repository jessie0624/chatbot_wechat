from weChat_conn import *

class MyWeChat(weChat):
    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
            #self.send_msg_by_uid(u'hi', msg['user']['id'])
            log('hi', 'info')

def main():
    mybot = MyWeChat()
    mybot.DEBUG = True
    mybot.conf['qr'] = 'png'
    mybot.run()

if __name__ == '__main__':
    main()