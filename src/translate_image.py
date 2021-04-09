import os
import cv2
import gdal

class TranslateImage(object):
    
    def __init__(self, output_file_format):
        self.output_file_format = output_file_format
        self.output_dir = '../output/'
    
    
    def crop_black_portion(self, img_path, output_file_name, unique_id):
        
        image = cv2.imread(img_path)
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        _,thresh = cv2.threshold(gray,1,255,cv2.THRESH_BINARY)
        
        b, g, r = cv2.split(image)
        
        rgba = [b,g,r, thresh]
        cropped_image = cv2.merge(rgba,4)

        file_name = os.path.join(unique_id, output_file_name + '_' + 'raw' + '.png')
        full_path = os.path.join(self.output_dir, file_name)
        
        success = cv2.imwrite(full_path, cropped_image)
        
        if not success:
            print("cv2.imwrite: crop failed")
            abort(500, "Internal Server Error")

        return file_name
        

    def translate_image(self):
        
        kwargs = {
            'format': self.output_file_format
        }
        

        for unique_id_dir in os.listdir(self.output_dir):
            for img_file in os.listdir(os.path.join(self.output_dir, unique_id_dir)):
                file_name = img_file.split('.')[0]
                if os.path.exists(os.path.join(self.output_dir, unique_id_dir, file_name + '.png')):
                    continue
                
                png_path = os.path.join(self.output_dir, unique_id_dir, file_name + '.png')
                tif_path = os.path.join(self.output_dir, unique_id_dir, file_name + '.tif')
                
                # Translate from TIF to PNG
                gdal.Translate(png_path, tif_path, **kwargs)

                #abort(500, "translate done")

                # crop PNG
                cropped_img_file_name = self.crop_black_portion(png_path, file_name, unique_id_dir)

        return cropped_img_file_name