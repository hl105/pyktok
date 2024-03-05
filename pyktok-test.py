import pyktok
pyktok.specify_browser('chrome')
pyktok.save_tiktok_multi_urls(["https://www.tiktokv.com/share/video/7315561816673750318/","https://www.tiktokv.com/share/video/7314460767946837294/"], False, # save video file
                		   'tiktok_data.csv',
                		    5)