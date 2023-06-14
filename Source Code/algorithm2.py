def SDN_Detection_System(Traffic_Sequences):
    for sequence in Traffic_Sequences:
        if sequence == "ofp_packet_in":
            Packet_Features = feature_extraction(sequence)
            Result = DCNN(Packet_Features)
            if Result == 0:
                send_Packet_Out_Message()
            else:
                send_Log_to_Blacklists_Table()
        elif sequence == "ofp_flow_states_reply":
            Packet_Features = feature_extraction(sequence)
            if reply == 0:
                forward_Packet()
            else:
                send_Log_to_Blacklists_Table()
    IP_traceback(Blacklists)
    Action_Block_Attack_Port()

def feature_extraction(sequence):
    # Perform feature extraction on the given sequence
    # Return the extracted features

def DCNN(Packet_Features):
    # Implement the DCNN model and pass the Packet_Features as input
    # Return the result (0 or 1) indicating the detection result

def send_Packet_Out_Message():
    # Code to send Packet_Out message

def send_Log_to_Blacklists_Table():
    # Code to send the log to the Blacklists Table

def forward_Packet():
    # Code to forward the packet

def IP_traceback(Blacklists):
    # Code for IP traceback using the Blacklists

def Action_Block_Attack_Port():
    # Code to take action to block the attack port

# Call the SDN Detection System function with appropriate Traffic_Sequences input
SDN_Detection_System(Traffic_Sequences)
