class Solution {
    public int findComplement(int num) {
        String bin = Integer.toBinaryString(num);
        String comp = "0";
        for (int i = 1; i < bin.length(); i++){
            if (bin.charAt(i) == '1'){
                comp += 0;
            } else{
                comp += 1;
            }
        }
        return Integer.parseInt(comp, 2);
    }
}
