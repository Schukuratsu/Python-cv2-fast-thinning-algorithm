import cv2
import numpy as np

show_images = 1

def fastThin(img_ori):
  obj = 0
  bg = 255
  img = img_ori.copy()
  if(show_images):
    cv2.imshow('pre morphology',img)
  img = morphology(img)
  cleanCorners(img)
  if(show_images):
    cv2.imshow('morphology',img)
  eraseTwoByTwos(img)
  if(show_images):
    cv2.imshow('morphology + eraseTwoByTwos',img)
  eraseLadders(img)
  if(show_images):
    cv2.imshow('morphology + eraseTwoByTwos + eraseLadders',img)
  return img

def morphology(img):
  # inverts the image to execute easier operations (sum and subtraction)
  a, img = cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV) 
  # generates 3 by 3 cross kernel
  kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3)) 
  # iteration counter
  iteration = 0
  print "Starting fast thin..."
  while 1:
    iteration += 1
    print "Running iteration",iteration,"of morphology" # "Running iteration x"
    #erosion
    last_img = img.copy()
    ero = cv2.erode(img,kernel,iterations = 1)
    #dilation
    dil = cv2.dilate(ero,kernel,iterations = 1)
    # result = original - dilated + eroded
    img -= dil
    img += ero
    # ends loop if result is the same from last iteration
    if cv2.compare(img, last_img, cv2.CMP_EQ).all():
      break
  a, img = cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV) # inverts back the image
  return img

# came up with this one by myself, if anyone finds a better way of detecting/reducing interest areas please tell me
def eraseTwoByTwos(img):
  altura = img.shape[0]
  largura = img.shape[1]
  obj = 0
  bg = 255
  for y in xrange(1,altura-2):
    for x in xrange(1,largura-2):
      #centrais
      c1 = img[y,x]
      c2 = img[y,x+1]
      c3 = img[y+1,x]
      c4 = img[y+1,x+1]
      if(c1 == obj and c2 == obj and c3 == obj and c4 == obj):
        if img[y-1,x-1]!=obj:
          img[y,x] = bg
          pass
        elif img[y-1,x+2]!=obj:
          img[y,x+1]=bg
          pass
        elif img[y+2,x-1]!=obj:
          img[y+1,x]=bg
          pass
        elif img[y+2,x+2]!=obj:
          img[y+1,x+1]=bg
          pass
        #vizinhos
        v1  = img[y-1,x-1]
        v2  = img[y-1,x]
        v3  = img[y-1,x+1]
        v4  = img[y-1,x+2]
        v5  = img[y,x+2]
        v6  = img[y+1,x+2]
        v7  = img[y+2,x+2]
        v8  = img[y+2,x+1]
        v9  = img[y+2,x]
        v10 = img[y+2,x-1]
        v11 = img[y+1,x-1]
        v12 = img[y,x-1]
        vizinhos = [v12,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11]

# sets the borders of the image as bg
def cleanCorners(img):
  altura = img.shape[0]
  largura = img.shape[1]
  bg = 255
  img[0:altura,0] = bg
  img[0,0:largura] = bg
  img[0:altura,largura-1] = bg
  img[altura-1,0:largura] = bg

# used in Zhang Suen algorithms to eliminate undesired corners
def eraseLadders(img):
  altura = img.shape[0]
  largura = img.shape[1]
  obj = 0
  bg = 255
  m1 = [[255,0,7  ],
        [0,  0,7  ],
        [7,  7,255]]
  m2 = [[7,  0,255],
        [7,  0,0  ],
        [255,7,7  ]]
  m3 = [[7,  7,255],
        [0,  0,7  ],
        [255,0,7  ]]
  m4 = [[255,7,7  ],
        [7,  0,0  ],
        [7,  0,255]]
  mask = [m1,m2,m3,m4]
  for y in xrange(1,altura-1):
    for x in xrange(1,largura-1):
      p5 = img[y,x]
      if p5 == obj:
        p1 = img[y-1,x-1]
        p2 = img[y-1,x]
        p3 = img[y-1,x+1]
        p4 = img[y,x-1]
        p6 = img[y,x+1]
        p7 = img[y+1,x-1]
        p8 = img[y+1,x]
        p9 = img[y+1,x+1]
        p = [[p1,p2,p3],
             [p4,p5,p6],
             [p7,p8,p9]]
        for m in mask:
          pairing = 1
          for i in xrange(0,3):
            for j in xrange(0,3):
              if m[i][j] != 7:
                if m[i][j] != p[i][j]:
                  pairing = 0
          if pairing:
            img[y,x] = bg
            break
