import os
import shutil
import cv2
import numpy as np
import argparse

def mix(img1, img2) :
    beta  = 0.5
    alpha = 1 - beta
    mixed = cv2.addWeighted(src1=img1, alpha=alpha,
                            src2=img2, beta=beta,
                            gamma=0)
    return mixed

def main():
    parser = argparse.ArgumentParser(description = "TrainArgs")
    parser.add_argument('file', type=str, help='path to image file')
    parser.add_argument('num_img', type=int, default=16,  help='number of result files')
    parser.add_argument('save_path', type=str, default="save_path", help="path to save directory")
    parser.add_argument('--mix', action='store_true')
    args = parser.parse_args()

    # Make empty directory
    if not os.path.exists(args.save_path) :
        os.mkdir(args.save_path)
    else :
        shutil.rmtree(args.save_path)
        os.mkdir(args.save_path)

    img = cv2.imread(args.file)
    n = args.num_img
    l_img = []

    # Change HSV value
    for i in range(n) :
        c = i*(180//n)%180
        #print(c)
        hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        hsv = hsv.astype(np.uint16)
        hsv[:,:,0] = (hsv[:,:,0]+c)%180
        hsv = hsv.astype(np.uint8)
        dst = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
        l_img.append(dst)

    # Save images
    file_name = args.file.split('/')[-1] # clip file name
    for i, data in enumerate(l_img) :
        save_path = args.save_path+"/"+str(i).zfill(3)+"_"+file_name
        cv2.imwrite(save_path, data, [cv2.IMWRITE_JPEG_QUALITY,100])
        if args.mix :
            next_data = l_img[i+1] if i != len(l_img)-1 else l_img[0]
            mix_name  = file_name.split('.')[0]+"Mix."+file_name.split('.')[1] # make mixed file name
            save_path = args.save_path+"/"+str(i).zfill(3)+"_"+mix_name
            mix_data = mix(data, next_data)
            cv2.imwrite(save_path, mix_data, [cv2.IMWRITE_JPEG_QUALITY,100])

if __name__ == '__main__' :
    main()
