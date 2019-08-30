class Test:
    # 高德
    gd_main_url = 'https://surl.amap.com/4kS7TFI1Mj'
    gd_main_url_net = 'https://ditu.amap.com/detail/get/detail?id=B0FFIPJE9Z'  # 搜索-network
    gd_cai_url_net = 'https://ditu.amap.com/detail/get/detail?id=B0FFF4VIBD'  # 搜索-network
    gd_main_url_search = 'https://www.amap.com/service/poiInfo?query_type=IDQ&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=18&id=B0FFIPJE9Z&city=150925&geoobj=112.495651%7C40.524669%7C112.499979%7C40.526305&keywords=%E8%B5%B5%E5%9B%9B%E9%A5%B8%E9%A5%B9%E9%9D%A2'
    gd_cai_url = 'https://surl.amap.com/4jViED1j7T9'  # 分享链接
    gd_cai_map_search = 'http://wb.amap.com/?p=B0FFF4VIBD%2C40.526855%2C112.503824%2C%E6%B4%BB%E9%B1%BC%E5%86%9C%E5%AE%B6%E8%8F%9C%2C%E4%B9%8C%E5%85%B0%E5%AF%9F%E5%B8%83%E5%B8%82%E5%87%89%E5%9F%8E%E5%8E%BF%E9%B8%BF%E8%8C%85%E9%95%87%E5%AE%A3%E5%BE%B7%E8%A1%97'  # 搜索-network
    gd_cai_url_search = 'https://www.amap.com/service/poiInfo?query_type=IDQ&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=18.92&city=150925&id=B0FFF4VIBD&keywords=%E6%B4%BB%E9%B1%BC%E5%86%9C%E5%AE%B6%E8%8F%9C'  # 搜索-network
    # gd_cai_search_json = 'https://ditu.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=9&city=150000&geoobj=111.369628%7C40.109789%7C113.566917%7C40.940696&keywords=%E6%B4%BB%E9%B1%BC%E5%86%9C%E5%AE%B6%E8%8F%9C'  # 搜索-network
    gd_cai_search_json = 'https://www.amap.com/service/poiInfo?query_type=IDQ&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=18&id=B0FFIPJE9Z&city=150925&geoobj=112.501691%7C40.530944%7C112.505983%7C40.532248&keywords=%E8%B5%B5%E5%9B%9B%E9%A5%B8%E9%A5%B9%E9%9D%A2'  # 搜索-network
    # gd_mian_url = 'https://www.amap.com/place/B0FFF4VIBD'#网页链接1
    # gd_mian_url = 'https://m.amap.com/search/mapview/poiid=B0FFF4VIBD'#网页链接2
    # gd_main_url_in_json = 'http://wb.amap.com/?p=B0FFF4VIBD%2C40.526855%2C112.503824%2C%E6%B4%BB%E9%B1%BC%E5%86%9C%E5%AE%B6%E8%8F%9C%2C%E4%B9%8C%E5%85%B0%E5%AF%9F%E5%B8%83%E5%B8%82%E5%87%89%E5%9F%8E%E5%8E%BF%E9%B8%BF%E8%8C%85%E9%95%87%E5%AE%A3%E5%BE%B7%E8%A1%97'  # json里面的分享地址
    # 百度
    bd_cai_url = 'http://j.map.baidu.com/10/zZd'
    bd_cai_url = 'https://map.baidu.com/search/%E6%B4%BB%E9%B1%BC%E5%86%9C%E5%AE%B6%E8%8F%9C/@12970743,4843033,13z?querytype=inf&uid=ae9081579d93b6fc6e20b953&c=131&da_src=shareurl'
    bd_main_url = 'http://j.map.baidu.com/38/aPd'


cookie_list = [
    # 'cna=O9XoEo6ZhyUCAdrMfznvRD2P; guid=5433-9edf-297a-6ed7; UM_distinctid=16b49aaccbc3c-0ff7f491f7b832-1333063-e1000-16b49aaccbd49; _uab_collina=156464561209613826862645; CNZZDATA1255827602=1589352391-1564726128-https%253A%252F%252Fwww.amap.com%252F%7C1564726128; key=bfe31f4e0fb231d29e1d3ce951e2c780; Hm_lvt_cdce8cda34e84469b1c8015204129522=1564895489; Hm_lpvt_cdce8cda34e84469b1c8015204129522=1564895489; CNZZDATA1255626299=871072546-1564894908-%7C1564894908; x5sec=7b22617365727665723b32223a223531656337333439643466353933383731333536643665363639653236626436434e72536d656f46454c37552b4b664c6f4b47757851453d227d; l=cBOtioynqU3Mpu3oBOfNiuIRtH_t2IRff1Pzw4iuHICP9LIH58MVWZFrx3vMCnGVK6SpQ3SgKvQUByTdgyCqM24dJx8wCO5..; isg=BLS0wKE2VaGjysFtlwYpGtjxhXLmJR_kzEWXJk4V9z_CuVMDUZ0qBw47PbHERhDP',
    # 'cna=O9XoEo6ZhyUCAdrMfznvRD2P; guid=5433-9edf-297a-6ed7; UM_distinctid=16b49aaccbc3c-0ff7f491f7b832-1333063-e1000-16b49aaccbd49; CNZZDATA1255827602=1951152380-1564557902-https%253A%252F%252Fditu.amap.com%252F%7C1564651404; key=bfe31f4e0fb231d29e1d3ce951e2c780; CNZZDATA1255626299=779622213-1564556767-%7C1564894908; Hm_lvt_cdce8cda34e84469b1c8015204129522=1564560748,1564655508,1564898807; Hm_lpvt_cdce8cda34e84469b1c8015204129522=1564898807; x5sec=7b22617365727665723b32223a223364306432313533623830656563393430326131346238326434366634303864434b58736d656f46454a432f72657a4c6f4b6e554a513d3d227d; l=cBOtioynqU3MpSl8BOfwGuIRtH_T6BOX1sPzw4iuHICPOofv5iEdWZFrkw8JCnGVLsNX83SgKvQUBW8LpyUIhQs33ge-_g4N.; isg=BDMz69dRapwHHyZIvAOmN9NMwjedwAC5Vwjww-XX9dKJ5F-GbjjmeisynlSvxB8i',
    # 'cna=O9XoEo6ZhyUCAdrMfznvRD2P; guid=5433-9edf-297a-6ed7; UM_distinctid=16b49aaccbc3c-0ff7f491f7b832-1333063-e1000-16b49aaccbd49; CNZZDATA1255827602=1951152380-1564557902-https%253A%252F%252Fditu.amap.com%252F%7C1564651404; key=bfe31f4e0fb231d29e1d3ce951e2c780; CNZZDATA1255626299=779622213-1564556767-%7C1564894908; Hm_lvt_cdce8cda34e84469b1c8015204129522=1564560748,1564655508,1564898807; Hm_lpvt_cdce8cda34e84469b1c8015204129522=1564898807; x5sec=7b22617365727665723b32223a223364306432313533623830656563393430326131346238326434366634303864434b58736d656f46454a432f72657a4c6f4b6e554a513d3d227d; l=cBOtioynqU3MpIVFBOfwmuIRtH_9VLAXGsPzw4iuHICP9M5D5iEdWZFr8EYkCnGVK6qv83SgKvQUB_4BqyCV3lgR8yIAhKC..; isg=BKenhPuVtvi9TjJ0AEdqU-fANtuxhLydA_QEH3ke5jZdaMoqgvxzXmUuiijTgFOG',
    'cna=O9XoEo6ZhyUCAdrMfznvRD2P; guid=5433-9edf-297a-6ed7; UM_distinctid=16b49aaccbc3c-0ff7f491f7b832-1333063-e1000-16b49aaccbd49; sc_is_visitor_unique=rx10852108.1564655725.50C3CEE769174F68D399BBA5C6BE3C70.2.2.2.2.2.2.2.1.1; key=bfe31f4e0fb231d29e1d3ce951e2c780; Hm_lvt_cdce8cda34e84469b1c8015204129522=1564560537,1564655504,1564898103; isg=BCcnBHsVNng-T7L0gMfq02dAtlsxBDwdg3SEn_mZOrbd6EqqAnzz3uWhCqhTANMG; l=cBOtioynqU3Mp9FOBOfNcuIRtH_tWdOXGsPzw4iuHICP9D5D5iEdWZFrRr8kCnGVK6uB83SgKvQUB_4BqyCC3lgR8R6EdDf..; x5sec=7b22617365727665723b32223a223033636266616361303930346139666265393563666164353332343863653237434a43416d756f46454a54776874694970364c4f3177453d227d; Hm_lpvt_cdce8cda34e84469b1c8015204129522=1564901406',
    # 'isg=BL29UFpHvJoQtBjyLdbU7CmdxBm3WvGsR4dhyX8BLZRDttDoVaqkfMIoYChVLQlk; l=cBNb-wucqYoeNEKUBOfC-urza779zQd6CkPzaNbMiICPO6BW5GbPWZFrRbxXCn1AK6a6x3RX67qwBR8dxyCweePmFC1hE_1..; key=bfe31f4e0fb231d29e1d3ce951e2c780; guid=5956-4981-dc94-d86f; UM_distinctid=16c5b51e1321f5-0db49fdfe92082-5f1a4044-e1000-16c5b51e13320d; cna=W2nNFQuJoX8CAd6B6Pnet0zm; CNZZDATA1255626299=2140005011-1564650885-%7C1564896500; _uab_collina=156490018979763400688918',
]

#
# cna=O9XoEo6ZhyUCAdrMfznvRD2P;
# guid=5433-9edf-297a-6ed7;
# UM_distinctid=16b49aaccbc3c-0ff7f491f7b832-1333063-e1000-16b49aaccbd49;
# _uab_collina=156464561209613826862645;
# CNZZDATA1255827602=1589352391-1564726128-https%253A%252F%252Fwww.amap.com%252F%7C1564726128;
# key=bfe31f4e0fb231d29e1d3ce951e2c780;
# Hm_lvt_cdce8cda34e84469b1c8015204129522=1564895489;
# Hm_lpvt_cdce8cda34e84469b1c8015204129522=1564895489;
# CNZZDATA1255626299=871072546-1564894908-%7C1564894908;
# x5sec=7b22617365727665723b32223a223531656337333439643466353933383731333536643665363639653236626436434e72536d656f46454c37552b4b664c6f4b47757851453d227d;
# l=cBOtioynqU3Mpu3oBOfNiuIRtH_t2IRff1Pzw4iuHICP9LIH58MVWZFrx3vMCnGVK6SpQ3SgKvQUByTdgyCqM24dJx8wCO5..;
# isg=BLS0wKE2VaGjysFtlwYpGtjxhXLmJR_kzEWXJk4V9z_CuVMDUZ0qBw47PbHERhDP
#
# cna=O9XoEo6ZhyUCAdrMfznvRD2P;
# guid=5433-9edf-297a-6ed7;
# UM_distinctid=16b49aaccbc3c-0ff7f491f7b832-1333063-e1000-16b49aaccbd49;
# CNZZDATA1255827602=1951152380-1564557902-https%253A%252F%252Fditu.amap.com%252F%7C1564651404;
# key=bfe31f4e0fb231d29e1d3ce951e2c780;
# CNZZDATA1255626299=779622213-1564556767-%7C1564894908;
# Hm_lvt_cdce8cda34e84469b1c8015204129522=1564560748,1564655508,1564898807;
# Hm_lpvt_cdce8cda34e84469b1c8015204129522=1564898807;
# x5sec=7b22617365727665723b32223a223364306432313533623830656563393430326131346238326434366634303864434b58736d656f46454a432f72657a4c6f4b6e554a513d3d227d;
# l=cBOtioynqU3MpSl8BOfwGuIRtH_T6BOX1sPzw4iuHICPOofv5iEdWZFrkw8JCnGVLsNX83SgKvQUBW8LpyUIhQs33ge-_g4N.;
# isg=BDMz69dRapwHHyZIvAOmN9NMwjedwAC5Vwjww-XX9dKJ5F-GbjjmeisynlSvxB8i
#
# cna=O9XoEo6ZhyUCAdrMfznvRD2P;
# guid=5433-9edf-297a-6ed7;
# UM_distinctid=16b49aaccbc3c-0ff7f491f7b832-1333063-e1000-16b49aaccbd49;
# CNZZDATA1255827602=1951152380-1564557902-https%253A%252F%252Fditu.amap.com%252F%7C1564651404;
# key=bfe31f4e0fb231d29e1d3ce951e2c780;
# CNZZDATA1255626299=779622213-1564556767-%7C1564894908;
# Hm_lvt_cdce8cda34e84469b1c8015204129522=1564560748,1564655508,1564898807;
# Hm_lpvt_cdce8cda34e84469b1c8015204129522=1564898807;
# x5sec=7b22617365727665723b32223a223364306432313533623830656563393430326131346238326434366634303864434b58736d656f46454a432f72657a4c6f4b6e554a513d3d227d;
# l=cBOtioynqU3MpIVFBOfwmuIRtH_9VLAXGsPzw4iuHICP9M5D5iEdWZFr8EYkCnGVK6qv83SgKvQUB_4BqyCV3lgR8yIAhKC..;
# isg=BKenhPuVtvi9TjJ0AEdqU-fANtuxhLydA_QEH3ke5jZdaMoqgvxzXmUuiijTgFOG
