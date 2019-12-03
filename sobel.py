def sobel():
    img = cv2.imread("a.jpg",flags=cv2.IMREAD_GRAYSCALE)
    cv2.imwrite("aa.jpg",img)
    h,w = img.shape
    kernel_x = np.array([-1,0,1,-2,0,2,-1,0,1])
    img_shape = img.shape
    mask = np.zeros(img_shape,dtype=np.int32)
    for i in range(1,h-1):
        for j in range(1,w-1):
            eight_pix = np.array([img[i-1,j-1],img[i-1,j],img[i-1,j+1],
                                  img[i,j-1],img[i,j],img[i,j+1],
                                  img[i+1,j+1],img[i+1,j],img[i+1,j+1]])
            mask[i,j] = np.dot(kernel_x,eight_pix)
    mask = abs(mask)
    mask = mask.astype(np.uint8)
    img2[:,:,0] = mask+img2[:,:,0]
    img2[:,:,1] = mask+img2[:,:,1]
    img2[:,:,2] = mask+img2[:,:,2]
    cv2.imwrite("sharp.jpg",mask)
