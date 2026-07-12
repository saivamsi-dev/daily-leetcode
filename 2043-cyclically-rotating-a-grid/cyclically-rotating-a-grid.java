// class Solution {
//     public int[][] rotateGrid(int[][] grid, int k) {
        
//     }
// }
class Solution {
    public int[][] rotateGrid(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        int numLayers = Math.min(m, n) / 2;
        
        for (int layer = 0; layer < numLayers; layer++) {
            // Define boundaries for the current layer
            int top = layer;
            int bottom = m - 1 - layer;
            int left = layer;
            int right = n - 1 - layer;
            
            // 1. Count total elements in this layer's perimeter
            int perimeter = 2 * (bottom - top + 1) + 2 * (right - left + 1) - 4;
            int[] elements = new int[perimeter];
            int idx = 0;
            
            // Extract elements in counter-clockwise order
            // Top row (left to right)
            for (int j = left; j <= right; j++) elements[idx++] = grid[top][j];
            // Right column (top + 1 to bottom)
            for (int i = top + 1; i <= bottom; i++) elements[idx++] = grid[i][right];
            // Bottom row (right - 1 down to left)
            for (int j = right - 1; j >= left; j--) elements[idx++] = grid[bottom][j];
            // Left column (bottom - 1 down to top + 1)
            for (int i = bottom - 1; i > top; i--) elements[idx++] = grid[i][left];
            
            // 2. Optimize rotation using modulo arithmetic
            int effectiveK = k % perimeter;
            
            // 3. Put elements back into the grid with a counter-clockwise shift
            idx = 0;
            
            // Top row
            for (int j = left; j <= right; j++) {
                grid[top][j] = elements[(idx + effectiveK) % perimeter];
                idx++;
            }
            // Right column
            for (int i = top + 1; i <= bottom; i++) {
                grid[i][right] = elements[(idx + effectiveK) % perimeter];
                idx++;
            }
            // Bottom row
            for (int j = right - 1; j >= left; j--) {
                grid[bottom][j] = elements[(idx + effectiveK) % perimeter];
                idx++;
            }
            // Left column
            for (int i = bottom - 1; i > top; i--) {
                grid[i][left] = elements[(idx + effectiveK) % perimeter];
                idx++;
            }
        }
        
        return grid;
    }
}