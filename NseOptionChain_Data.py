import requests
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


class NseIndia2:

    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
        self.session = requests.Session()
        self.session.get("http://nseindia.com", headers=self.headers)

    def get_option_chain(self, symbol, indices=False):
        url = 'https://www.nseindia.com/api/option-chain-equities?symbol=' + symbol
        data = self.session.get(url,headers=self.headers).json()["records"]["data"]
        # my_df = []
        # for i in data:
        #     for k, v in i.items():
        #         if k == "CE" or k == "PE":
        #             info = v
        #             info["instrumentType"] = k
        #             my_df.append(info)
        df=pd.DataFrame(data)
        df.to_csv("RAW_DATA.csv",index=False)
        ndf=pd.read_csv("RAW_DATA.csv")
        ndf=ndf.dropna()
        rows=len(ndf)
        # return pd.DataFrame(my_df)    
        

for i in range(0,rows):
        STKCE=ndf["CE"].iloc[i]
        STKCE=eval(STKCE)
        STKPE=ndf["PE"].iloc[i]
        STKPE=eval(STKPE)
        CEDF=pd.DataFrame(STKCE,index=[0])
        PEDF=pd.DataFrame(STKPE,index=[0])
        CEDF.to_csv("FILTERED_DATA.csv",index=False,mode='a',header=False)
        PEDF.to_csv("FILTERED_DATA.csv",index=False,mode='a',header=False)
    final=pd.read_csv("FILTERED_DATA.csv")
    final.columns=COL
    final.to_csv("FILTERED_DATA.csv",index=False)
    #os.system('copy FILTERED_DATA.csv LIVE_DATA.csv')
    shutil.copy('FILTERED_DATA.csv','LIVE_DATA.csv')
    
    os.remove('FILTERED_DATA.csv')
    os.remove('RAW_DATA.csv')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    ce1_ltp=final["LTP"][(final.SYMBOL==symbolce1)].to_string(index=False)
    ce1_iv=final["IV"][(final.SYMBOL==symbolce1)].to_string(index=False)
    ce1_oi=final["OI"][(final.SYMBOL==symbolce1)].to_string(index=False)
    ce1_ttv=final["TTV"][(final.SYMBOL==symbolce1)].to_string(index=False)
    ce1_choi=final["CHNGOI"][(final.SYMBOL==symbolce1)].to_string(index=False)
    
    ce1_stk=final["STK"][(final.SYMBOL==symbolce1)].to_string(index=False)      
    ce2_stk=final["STK"][(final.SYMBOL==symbolce2)].to_string(index=False)     
    ce3_stk=final["STK"][(final.SYMBOL==symbolce3)].to_string(index=False)     
    ce4_stk=final["STK"][(final.SYMBOL==symbolce4)].to_string(index=False)     
    ce5_stk=final["STK"][(final.SYMBOL==symbolce5)].to_string(index=False)     
    ce6_stk=final["STK"][(final.SYMBOL==symbolce6)].to_string(index=False)     
    ce7_stk=final["STK"][(final.SYMBOL==symbolce7)].to_string(index=False)     
    
    pe1_stk=final["STK"][(final.SYMBOL==symbolpe1)].to_string(index=False)      
    pe2_stk=final["STK"][(final.SYMBOL==symbolpe2)].to_string(index=False)     
    pe3_stk=final["STK"][(final.SYMBOL==symbolpe3)].to_string(index=False)     
    pe4_stk=final["STK"][(final.SYMBOL==symbolpe4)].to_string(index=False)     
    pe5_stk=final["STK"][(final.SYMBOL==symbolpe5)].to_string(index=False)     
    pe6_stk=final["STK"][(final.SYMBOL==symbolpe6)].to_string(index=False)     
    pe7_stk=final["STK"][(final.SYMBOL==symbolpe7)].to_string(index=False)   
    
    ce2_ltp=final["LTP"][(final.SYMBOL==symbolce2)].to_string(index=False)     
    ce2_iv=final["IV"][(final.SYMBOL==symbolce2)].to_string(index=False)     
    ce2_oi=final["OI"][(final.SYMBOL==symbolce2)].to_string(index=False)     
    ce2_ttv=final["TTV"][(final.SYMBOL==symbolce2)].to_string(index=False)     
    ce2_choi=final["CHNGOI"][(final.SYMBOL==symbolce2)].to_string(index=False)     
    
    ce3_ltp=final["LTP"][(final.SYMBOL==symbolce3)].to_string(index=False)     
    ce3_iv=final["IV"][(final.SYMBOL==symbolce3)].to_string(index=False)     
    ce3_oi=final["OI"][(final.SYMBOL==symbolce3)].to_string(index=False)     
    ce3_ttv=final["TTV"][(final.SYMBOL==symbolce3)].to_string(index=False)     
    ce3_choi=final["CHNGOI"][(final.SYMBOL==symbolce3)].to_string(index=False)     
    
    ce4_ltp=final["LTP"][(final.SYMBOL==symbolce4)].to_string(index=False)     
    ce4_iv=final["IV"][(final.SYMBOL==symbolce4)].to_string(index=False)     
    ce4_oi=final["OI"][(final.SYMBOL==symbolce4)].to_string(index=False)     
    ce4_ttv=final["TTV"][(final.SYMBOL==symbolce4)].to_string(index=False)     
    ce4_choi=final["CHNGOI"][(final.SYMBOL==symbolce4)].to_string(index=False)     
    
    ce5_ltp=final["LTP"][(final.SYMBOL==symbolce5)].to_string(index=False)     
    ce5_iv=final["IV"][(final.SYMBOL==symbolce5)].to_string(index=False)     
    ce5_oi=final["OI"][(final.SYMBOL==symbolce5)].to_string(index=False)     
    ce5_ttv=final["TTV"][(final.SYMBOL==symbolce5)].to_string(index=False)     
    ce5_choi=final["CHNGOI"][(final.SYMBOL==symbolce5)].to_string(index=False)     
    
    ce6_ltp=final["LTP"][(final.SYMBOL==symbolce6)].to_string(index=False)     
    ce6_iv=final["IV"][(final.SYMBOL==symbolce6)].to_string(index=False)     
    ce6_oi=final["OI"][(final.SYMBOL==symbolce6)].to_string(index=False)     
    ce6_ttv=final["TTV"][(final.SYMBOL==symbolce6)].to_string(index=False)     
    ce6_choi=final["CHNGOI"][(final.SYMBOL==symbolce6)].to_string(index=False)     
    
    ce7_ltp=final["LTP"][(final.SYMBOL==symbolce7)].to_string(index=False)     
    ce7_iv=final["IV"][(final.SYMBOL==symbolce7)].to_string(index=False)     
    ce7_oi=final["OI"][(final.SYMBOL==symbolce7)].to_string(index=False)     
    ce7_ttv=final["TTV"][(final.SYMBOL==symbolce7)].to_string(index=False)     
    ce7_choi=final["CHNGOI"][(final.SYMBOL==symbolce7)].to_string(index=False)     
    
    pe1_ltp=final["LTP"][(final.SYMBOL==symbolpe1)].to_string(index=False)     
    pe1_iv=final["IV"][(final.SYMBOL==symbolpe1)].to_string(index=False)     
    pe1_oi=final["OI"][(final.SYMBOL==symbolpe1)].to_string(index=False)     
    pe1_ttv=final["TTV"][(final.SYMBOL==symbolpe1)].to_string(index=False)     
    pe1_choi=final["CHNGOI"][(final.SYMBOL==symbolpe1)].to_string(index=False)     
    
    pe2_ltp=final["LTP"][(final.SYMBOL==symbolpe2)].to_string(index=False)     
    pe2_iv=final["IV"][(final.SYMBOL==symbolpe2)].to_string(index=False)     
    pe2_oi=final["OI"][(final.SYMBOL==symbolpe2)].to_string(index=False)     
    pe2_ttv=final["TTV"][(final.SYMBOL==symbolpe2)].to_string(index=False)     
    pe2_choi=final["CHNGOI"][(final.SYMBOL==symbolpe2)].to_string(index=False)     
    
    pe3_ltp=final["LTP"][(final.SYMBOL==symbolpe3)].to_string(index=False)     
    pe3_iv=final["IV"][(final.SYMBOL==symbolpe3)].to_string(index=False)     
    pe3_oi=final["OI"][(final.SYMBOL==symbolpe3)].to_string(index=False)     
    pe3_ttv=final["TTV"][(final.SYMBOL==symbolpe3)].to_string(index=False)     
    pe3_choi=final["CHNGOI"][(final.SYMBOL==symbolpe3)].to_string(index=False)     
    
    pe4_ltp=final["LTP"][(final.SYMBOL==symbolpe4)].to_string(index=False)     
    pe4_iv=final["IV"][(final.SYMBOL==symbolpe4)].to_string(index=False)     
    pe4_oi=final["OI"][(final.SYMBOL==symbolpe4)].to_string(index=False)     
    pe4_ttv=final["TTV"][(final.SYMBOL==symbolpe4)].to_string(index=False)     
    pe4_choi=final["CHNGOI"][(final.SYMBOL==symbolpe4)].to_string(index=False)     
    
    pe5_ltp=final["LTP"][(final.SYMBOL==symbolpe5)].to_string(index=False)     
    pe5_iv=final["IV"][(final.SYMBOL==symbolpe5)].to_string(index=False)     
    pe5_oi=final["OI"][(final.SYMBOL==symbolpe5)].to_string(index=False)     
    pe5_ttv=final["TTV"][(final.SYMBOL==symbolpe5)].to_string(index=False)     
    pe5_choi=final["CHNGOI"][(final.SYMBOL==symbolpe5)].to_string(index=False)     
    
    pe6_ltp=final["LTP"][(final.SYMBOL==symbolpe6)].to_string(index=False)     
    pe6_iv=final["IV"][(final.SYMBOL==symbolpe6)].to_string(index=False)     
    pe6_oi=final["OI"][(final.SYMBOL==symbolpe6)].to_string(index=False)     
    pe6_ttv=final["TTV"][(final.SYMBOL==symbolpe6)].to_string(index=False)     
    pe6_choi=final["CHNGOI"][(final.SYMBOL==symbolpe6)].to_string(index=False)     
    
    pe7_ltp=final["LTP"][(final.SYMBOL==symbolpe7)].to_string(index=False)     
    pe7_iv=final["IV"][(final.SYMBOL==symbolpe7)].to_string(index=False)     
    pe7_oi=final["OI"][(final.SYMBOL==symbolpe7)].to_string(index=False)     
    pe7_ttv=final["TTV"][(final.SYMBOL==symbolpe7)].to_string(index=False)     
    pe7_choi=final["CHNGOI"][(final.SYMBOL==symbolpe7)].to_string(index=False)     
   
    DIX={"TIME":current_time,"ce1_stk":[ce1_stk],"ce1_ltp":[ce1_ltp],"ce1_iv":[ce1_iv],"ce1_oi":[ce1_oi],"ce1_ttv":[ce1_ttv],"ce1_choi":[ce1_choi],
         "ce2_stk":[ce2_stk],"ce2_ltp":[ce2_ltp],"ce2_iv":[ce2_iv],"ce2_oi":[ce2_oi],"ce2_ttv":[ce2_ttv],"ce2_choi":[ce2_choi],
         "ce3_stk":[ce3_stk],"ce3_ltp":[ce3_ltp],"ce3_iv":[ce3_iv],"ce3_oi":[ce3_oi],"ce3_ttv":[ce3_ttv],"ce3_choi":[ce3_choi],
         "ce4_stk":[ce4_stk],"ce4_ltp":[ce4_ltp],"ce4_iv":[ce4_iv],"ce4_oi":[ce4_oi],"ce4_ttv":[ce4_ttv],"ce4_choi":[ce4_choi],
         "ce5_stk":[ce5_stk],"ce5_ltp":[ce5_ltp],"ce5_iv":[ce5_iv],"ce5_oi":[ce5_oi],"ce5_ttv":[ce5_ttv],"ce5_choi":[ce5_choi],
         "ce6_stk":[ce6_stk],"ce6_ltp":[ce6_ltp],"ce6_iv":[ce6_iv],"ce6_oi":[ce6_oi],"ce6_ttv":[ce6_ttv],"ce6_choi":[ce6_choi],
         "ce7_stk":[ce7_stk],"ce7_ltp":[ce7_ltp],"ce7_iv":[ce7_iv],"ce7_oi":[ce7_oi],"ce7_ttv":[ce7_ttv],"ce7_choi":[ce7_choi],
         "pe1_stk":[pe1_stk],"pe1_ltp":[pe1_ltp],"pe1_iv":[pe1_iv],"pe1_oi":[pe1_oi],"pe1_ttv":[pe1_ttv],"pe1_choi":[pe1_choi],
         "pe2_stk":[pe2_stk],"pe2_ltp":[pe2_ltp],"pe2_iv":[pe2_iv],"pe2_oi":[pe2_oi],"pe2_ttv":[pe2_ttv],"pe2_choi":[pe2_choi],
         "pe3_stk":[pe3_stk],"pe3_ltp":[pe3_ltp],"pe3_iv":[pe3_iv],"pe3_oi":[pe3_oi],"pe3_ttv":[pe3_ttv],"pe3_choi":[pe3_choi],
         "pe4_stk":[pe4_stk],"pe4_ltp":[pe4_ltp],"pe4_iv":[pe4_iv],"pe4_oi":[pe4_oi],"pe4_ttv":[pe4_ttv],"pe4_choi":[pe4_choi],
         "pe5_stk":[pe5_stk],"pe5_ltp":[pe5_ltp],"pe5_iv":[pe5_iv],"pe5_oi":[pe5_oi],"pe5_ttv":[pe5_ttv],"pe5_choi":[pe5_choi],
         "pe6_stk":[pe6_stk],"pe6_ltp":[pe6_ltp],"pe6_iv":[pe6_iv],"pe6_oi":[pe6_oi],"pe6_ttv":[pe6_ttv],"pe6_choi":[pe6_choi],
         "pe7_stk":[pe7_stk],"pe7_ltp":[pe7_ltp],"pe7_iv":[pe7_iv],"pe7_oi":[pe7_oi],"pe7_ttv":[pe7_ttv],"pe7_choi":[pe7_choi]}
         
    FINAL=pd.DataFrame(DIX)
    FINAL.to_csv("LIVE_RECORD.csv",mode="a",index=False,header=False)
    print(current_time+' '+'DATA RECORDED SUCCESSFULLY')
    time.sleep(INTERVAL*60)
    
for j in range(0,int(REPEAT_CODE)):
    while True:
        try:
            DATA_EXTRACT()
            break
        except:
            print("Trying to collect data")
            time.sleep(5)
nse = NseIndia2()
print(nse.get_option_chain("ZEEL"))



