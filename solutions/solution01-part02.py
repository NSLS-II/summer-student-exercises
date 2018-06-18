plt.figure(2);


plt.clf(); # clear figure in case it's been drawn before
plt.imshow(img)

# use mask to mask out bad pixels
plt.figure(3);
plt.clf(); # clear figure in case it's been drawn before
plt.imshow(img*mask)