class user_room():
    user_id="null"
    msgs=[["Hi, how can I help you?", 'admin']]
    
    def admin_msg(msg):
        msgs.append([msg, 'admin'])
    
    def user_msg(msg):
        msgs.append([msg, 'user', lat, lng])

    def getmsg():
        return jsonify(msgs)