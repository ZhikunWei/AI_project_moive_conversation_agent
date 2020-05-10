from MyBot import MoiveConversationManager
from nlu_pipeline import nlu_subsystem
from nlg_pipeline import nlg_subsystem

if __name__ == '__main__':
    mcm = MoiveConversationManager()
    nlu = nlu_subsystem()
    nlg = nlg_subsystem()
    q = input('> Input: ')

    while q != 'q':
        try:
            nlu_data = nlu.process_sentence(q, log=True)
            print('nlu data', nlu_data)
            mcm.getDataFromNLU(nlu_data)
            result = mcm.getQueryResult()
            print('mcm', result)
            output = nlg.generate_answers(result)
            print('>', output)
        except Exception as e:
            print('conversation fail ', e)
        print('>>>>>>>>>>>>>>>>>>>>>>\nnew conversation\n>>>>>>>>>>>>>>>>>>')
        q = input('> Input: ')
