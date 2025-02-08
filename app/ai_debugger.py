import subprocess

def get_debugging_suggestions(code: str, model_name: str = "qwen2.5-coder:1.5b"):
    """
    Generate debugging suggestions using a locally hosted Ollama model.

    Args:
        code (str): The code snippet to debug.
        model_name (str): The name of the Ollama model to use (default: qwen2.5-coder:1.5b).

    Returns:
        str: AI-generated debugging suggestions.
    """
    prompt = f"Debug the following code:\n{code}\nProvide actionable suggestions for improvement."

    try:
        result = subprocess.run(
            ["ollama", "run", model_name, prompt],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error running Ollama model: {e.stderr}")
    except UnicodeDecodeError as e:
        raise Exception(f"Encoding error: {e}")


# if __name__ == "__main__":
#     code = """
#     class Solution {
#     public int[] queryResults(int limit, int[][] queries) {
#         Map<Integer, Integer> map = new HashMap<>();
        
#         Map<Integer, Integer> freq = new HashMap<>();

#         int len = queries.length;

#         int ans[] = new int[len];

#         int count = 0;

#         for(int i = 0; i < len; i++)
#         {
#             int first = queries[i][0];
#             int second = queries[i][1];


#             if(!map.containsKey(first))
#             {
#                 count++;
#                 map.put(first, second);
                
#             }

#             else
#             {
#                 int val = map.get(first);
#                 if(freq.get(val) == 1)
#                 {
#                     freq.remove(val);
#                 }
#                 else
#                 {
#                     freq.put(val, freq.get(val) - 1);
#                 }
#                 map.put(first, second);
#             }
#             freq.put(second, freq.getOrDefault(second, 0) + 1);

#             ans[i] = freq.size();
#         }

#         return ans;
#     }
# }
#     """
#     try:
#         suggestions = get_debugging_suggestions(code, model_name="qwen2.5-coder:1.5b")
#         print("AI Suggestions:", suggestions)
#     except Exception as e:
#         print("Error:", e)