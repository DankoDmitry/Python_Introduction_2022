# x = [14.5, 12.5, 17..25, 14.5, 12.625, 17.75, 14.125, 12.625]

g = [9.75, 8.375, 11, 9.75, 8.5, 12.5, 9, 8.5]
W = [27, 17, 41, 26, 17, 49, 23, 16]
print(sum(W[i] for i in range(len(W)))/sum(g[i]**3 for i in range(len(g))))

