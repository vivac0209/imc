# from PIL import Image
# image_file = Image.open("convert_image.png") # open colour image
# image_file = image_file.convert('L') # convert image to black and white
# image_file.save('result.png')

# PIL 套件中 Image的模組
# 處理圖片 把圖片轉成黑白
# image_file = image_file.convert('L')
# L是轉成灰色
# 1 是變成黑白 但畫素太差

# 這邊是一次把很多圖片轉灰色

from PIL import Image
import os


# for file in os.listdir('.'):		#這邊是把py檔資料夾中 所有的檔案都列出來
# 	if file.endswith('.jpg'):		# 把檔名是jpg結尾的 才要顯示出來
# 		print(file)

# orig 是原始圖的資料夾

# for file in os.listdir('orig'):		
# 	if file.endswith('.jpg'):		
# 		image_file = Image.open('orig/' + file) # 手動 因為程式檔的資料夾中還有orig資料夾 所以要給對路徑
# 		image_file = image_file.convert('L') # convert image to black and white
# 		image_file.save('result/' + file[:-4] + '_grey.png')			# 這邊是存檔功能 要設定不同的命名方式 不然多張圖片的名字無法都存成同一個名字
# file[:-4] 清單分割法 因為如果是image_file.save(file[:-4] + '_grey.png')	這樣
# 會存成 S__72966147.jpg_grey.png  .jpg都存進去了
# [-4] 把結尾.jpg去掉

# 另一種範例在資料夾路徑

for file in os.listdir('orig'):		
	if file.endswith('.jpg'):		
		image_file = Image.open(os.path.join('orig' , file)) # 使用os的join 去抓orig資料夾 
		image_file = image_file.convert('L') # convert image to black and white
		image_file.save(os.path.join('result' , file[:-4] + '_grey.png'))		