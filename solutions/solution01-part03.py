# SOLUTION

x0, y0 = md['x0'], md['y0']

plt.figure(4);
plt.clf()
plt.imshow(img)

# plot the beam center
plt.plot(x0, y0, 'ro')
# create phi
phi = np.linspace(0, 2*np.pi, 1000)
# now plot phi for a certain radius
for r in [10, 100, 200, 300, 400, 500]:
    plt.plot(r*np.cos(phi) + x0, r*np.sin(phi) + y0)