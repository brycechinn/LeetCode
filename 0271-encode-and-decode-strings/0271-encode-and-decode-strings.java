public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder stringBuilder = new StringBuilder();
        
        for (String str : strs) {
            int length = str.length();
            
            stringBuilder.append(String.valueOf(length));
            stringBuilder.append("#");
            stringBuilder.append(str);
        }
        
        System.out.println(stringBuilder.toString());
        
        return stringBuilder.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> result = new ArrayList<>();
        
        StringBuilder lengthBuilder = new StringBuilder();
        StringBuilder wordBuilder = new StringBuilder();
        
        int i = 0;
        while (i < s.length()) {
            char c = s.charAt(i);
            
            if (Character.isDigit(c)) {
                lengthBuilder.append(c);
                i++;
            } else if (c == '#') {
                int length = Integer.valueOf(lengthBuilder.toString());
                
                lengthBuilder = new StringBuilder();
                wordBuilder = new StringBuilder();
                
                i++;
                for (int j = i; j < i + length; j++) {
                    wordBuilder.append(s.charAt(j));
                }
                
                result.add(wordBuilder.toString());
                
                i += length;
            } else {
                i++;
            }   
        }
        
        return result;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));