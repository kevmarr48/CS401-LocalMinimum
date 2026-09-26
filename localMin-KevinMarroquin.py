"""
Group Members:
  - Kevin Marroquin
  - 
  - 
"""

import math

def LocalMinimum2D(arr):
  """
    Returns a local minimum for the given 2D input array.
    Must use divide and conquer

    Args:
      arr: a square (n x n) list of lists of distinct integers.
  """
  def isLocalMinimum(row, col):
      suspect = arr[row][col]

      return (suspect < arr[row][col - 1] and suspect < arr[row - 1][col] and suspect < arr[row + 1][col] and suspect < arr[row][col + 1]
      )


  def search(top, bottom, left, right, lowRow, lowCol):

      #find the midpoint of the current frame
      middleRow = (top + bottom) // 2
      middleCol = (left + right) // 2

      minRow = middleRow
      minCol = left + 1

      #minValue is the smallest value found in the row or col that found the midpopint
      minValue = arr[minRow][minCol]



      #cull through the row, looking for the smallest value
      for col in range(left + 1, right):
          if arr[middleRow][col] < minValue:
              minValue = arr[middleRow][col]
              minRow = middleRow
              minCol = col

      #cull through the col, looking for the smallest value
      for row in range(top + 1, bottom):
          if arr[row][middleCol] < minValue:
              minValue = arr[row][middleCol]
              minRow = row
              minCol = middleCol


      #check against the original value stored in lowRow and lowCol
      if minValue <= arr[lowRow][lowCol]:

          #base case
          if isLocalMinimum(minRow, minCol):
              return minValue

          #case: isnt a local minimum, grab the neighbors and find the smallest one
          neighbors = [(minRow - 1, minCol), (minRow + 1, minCol), (minRow, minCol - 1), (minRow, minCol + 1)]

          nextRow, nextCol = neighbors[0]

          #find the smallest neighbor
          for row, col in neighbors:
              if arr[row][col] < arr[nextRow][nextCol]:
                  nextRow = row
                  nextCol = col

      else:
          nextRow = lowRow
          nextCol = lowCol

      #set new bounds for the new cross and frame
      if nextRow < middleRow:
          newTop = top
          newBottom = middleRow
      else:
          newTop = middleRow
          newBottom = bottom


      if nextCol < middleCol:
          newLeft = left
          newRight = middleCol
      else:
          newLeft = middleCol
          newRight = right

      #recursive step
      return search(newTop, newBottom, newLeft, newRight, nextRow, nextCol)


  n = len(arr)

  #search the frame
  return search(0, n - 1, 0, n - 1, 1, 1)

if __name__ == "__main__":
  sample_input = [
    [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
    [math.inf, 9, 10, 7, 0, -2, math.inf],
    [math.inf, 3, 12, 5, 1, 17, math.inf],
    [math.inf, 11, 2, 14, 8, 6, math.inf],
    [math.inf, 4, -13, -10, 15, 90, math.inf],
    [math.inf, 45, 30, 20, 25, 60, math.inf],
    [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf]
  ]

  # any of -10, -2, 3, or 6 would be acceptable local minimums to return
  print(LocalMinimum2D(sample_input))