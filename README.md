Started with no hidden layers, just dense conections to see what was the output. I noticed a very fast computing time in comparation with every other one. But i got high loss and not great accuracy
Epoch 1/10
500/500 [==============================] - 2s 3ms/step - loss: 95.7166 - accuracy: 0.3930
Epoch 2/10
500/500 [==============================] - 2s 3ms/step - loss: 50.1364 - accuracy: 0.6112
Epoch 3/10
500/500 [==============================] - 2s 3ms/step - loss: 40.1155 - accuracy: 0.6872
Epoch 4/10
500/500 [==============================] - 2s 3ms/step - loss: 33.7406 - accuracy: 0.7275
Epoch 5/10
500/500 [==============================] - 2s 3ms/step - loss: 33.5100 - accuracy: 0.7526
Epoch 6/10
500/500 [==============================] - 2s 3ms/step - loss: 33.5037 - accuracy: 0.7690
Epoch 7/10
500/500 [==============================] - 2s 3ms/step - loss: 29.1062 - accuracy: 0.7918
Epoch 8/10
500/500 [==============================] - 2s 3ms/step - loss: 29.7514 - accuracy: 0.7987
Epoch 9/10
500/500 [==============================] - 2s 3ms/step - loss: 29.3916 - accuracy: 0.8124
Epoch 10/10
500/500 [==============================] - 2s 3ms/step - loss: 22.2031 - accuracy: 0.8364
333/333 - 1s - loss: 39.9264 - accuracy: 0.7672

Next added a hidden 128 layer dense connected with RELU activation and dropout of 0.5. This greatly reduced accurracy and loss.

Epoch 1/10
500/500 [==============================] - 4s 7ms/step - loss: 7.6710 - accuracy: 0.0537
Epoch 2/10
500/500 [==============================] - 3s 7ms/step - loss: 3.5877 - accuracy: 0.0561
Epoch 3/10
500/500 [==============================] - 3s 6ms/step - loss: 3.5384 - accuracy: 0.0560
Epoch 4/10
500/500 [==============================] - 3s 6ms/step - loss: 3.5153 - accuracy: 0.0564
Epoch 5/10
500/500 [==============================] - 3s 7ms/step - loss: 3.5047 - accuracy: 0.0566
Epoch 6/10
500/500 [==============================] - 3s 6ms/step - loss: 3.4998 - accuracy: 0.0571
Epoch 7/10
500/500 [==============================] - 3s 6ms/step - loss: 3.4974 - accuracy: 0.0551
Epoch 8/10
500/500 [==============================] - 3s 7ms/step - loss: 3.4961 - accuracy: 0.0565
Epoch 9/10
500/500 [==============================] - 3s 6ms/step - loss: 3.4955 - accuracy: 0.0552
Epoch 10/10
500/500 [==============================] - 3s 7ms/step - loss: 3.4952 - accuracy: 0.0571
333/333 - 1s - loss: 3.5037 - accuracy: 0.0552

In spite of reducing accurady, i wanted to keep loss reduction so i keeped the layer . Next Added a 2d convolutional layer with 32 filters and 3x3 kernel to see what happens. This didn’t improve either accuracy or loss. In fact it seems to make them slightly worse. And greatly increace computing time
Epoch 1/10
500/500 [==============================] - 40s 78ms/step - loss: 6.8785 - accuracy: 0.0497
Epoch 2/10
500/500 [==============================] - 37s 75ms/step - loss: 3.5864 - accuracy: 0.0525
Epoch 3/10
500/500 [==============================] - 37s 75ms/step - loss: 3.5392 - accuracy: 0.0539
Epoch 4/10
500/500 [==============================] - 39s 79ms/step - loss: 3.5119 - accuracy: 0.0553
Epoch 5/10
500/500 [==============================] - 39s 78ms/step - loss: 3.5009 - accuracy: 0.0556
Epoch 6/10
500/500 [==============================] - 40s 79ms/step - loss: 3.4957 - accuracy: 0.0566
Epoch 7/10
500/500 [==============================] - 37s 74ms/step - loss: 3.4933 - accuracy: 0.0559
Epoch 8/10
500/500 [==============================] - 36s 73ms/step - loss: 3.4920 - accuracy: 0.0556
Epoch 9/10
500/500 [==============================] - 36s 72ms/step - loss: 3.4914 - accuracy: 0.0547
Epoch 10/10
500/500 [==============================] - 39s 78ms/step - loss: 3.4911 - accuracy: 0.0543
333/333 - 4s - loss: 3.5092 - accuracy: 0.0502

Adding a max-pooling layer with 2x2 pool size to see if in combination with the last one improves something. Loss and accuracy got slightly better but not even close to the expectations. And a curious fact is that accuracy reached a fixed value after the third epoch. Computing time became faster.

Epoch 1/10
500/500 [==============================] - 18s 35ms/step - loss: 4.8282 - accuracy: 0.0543 
Epoch 2/10
500/500 [==============================] - 18s 36ms/step - loss: 3.5887 - accuracy: 0.0569
Epoch 3/10
500/500 [==============================] - 18s 36ms/step - loss: 3.5371 - accuracy: 0.0579
Epoch 4/10
500/500 [==============================] - 18s 35ms/step - loss: 3.5146 - accuracy: 0.0579
Epoch 5/10
500/500 [==============================] - 18s 36ms/step - loss: 3.5042 - accuracy: 0.0579
Epoch 6/10
500/500 [==============================] - 18s 35ms/step - loss: 3.4993 - accuracy: 0.0579
Epoch 7/10
500/500 [==============================] - 18s 36ms/step - loss: 3.4969 - accuracy: 0.0579
Epoch 8/10
500/500 [==============================] - 18s 35ms/step - loss: 3.4957 - accuracy: 0.0579
Epoch 9/10
500/500 [==============================] - 18s 35ms/step - loss: 3.4951 - accuracy: 0.0579
Epoch 10/10
500/500 [==============================] - 18s 35ms/step - loss: 3.4949 - accuracy: 0.0579
333/333 - 3s - loss: 3.5034 - accuracy: 0.0540

Adding another 2d convolutional layer with 32 filters and 3x3 kernel after the max-poolong. This greatly increased  accuracy and diminished loss. Computing time worsen again but it achieved a good result.

Epoch 1/10
500/500 [==============================] - 26s 50ms/step - loss: 3.0996 - accuracy: 0.3453 
Epoch 2/10
500/500 [==============================] - 25s 50ms/step - loss: 1.0343 - accuracy: 0.6923
Epoch 3/10
500/500 [==============================] - 25s 50ms/step - loss: 0.6239 - accuracy: 0.8171
Epoch 4/10
500/500 [==============================] - 27s 53ms/step - loss: 0.4434 - accuracy: 0.8676
Epoch 5/10
500/500 [==============================] - 26s 52ms/step - loss: 0.3704 - accuracy: 0.8909
Epoch 6/10
500/500 [==============================] - 23s 46ms/step - loss: 0.3181 - accuracy: 0.9060
Epoch 7/10
500/500 [==============================] - 22s 44ms/step - loss: 0.2577 - accuracy: 0.9266
Epoch 8/10
500/500 [==============================] - 24s 48ms/step - loss: 0.2409 - accuracy: 0.9304
Epoch 9/10
500/500 [==============================] - 24s 48ms/step - loss: 0.2214 - accuracy: 0.9356
Epoch 10/10
500/500 [==============================] - 25s 50ms/step - loss: 0.2447 - accuracy: 0.9334
333/333 - 5s - loss: 0.1315 - accuracy: 0.9718
