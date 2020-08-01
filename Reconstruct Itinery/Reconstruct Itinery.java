import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<String> findItinerary(List<List<String>> tickets) {
        Map<String, ArrayList<String>> map = new HashMap<String, ArrayList<String>>();
        for(List<String> trip:tickets){
            ArrayList<String> next_stops = map.getOrDefault(trip.get(0), null);
            if(next_stops != null){
                int index=0;
                while(index<next_stops.size() && trip.get(1).compareTo(next_stops.get(index)) >0 ) index++;
                next_stops.add(index, trip.get(1));
            }
            else{
                ArrayList<String> new_item = new ArrayList<>();
                new_item.add(trip.get(1));
                map.put(trip.get(0), new_item);
            }
        }

        List<String> res = new ArrayList<>();
        String str = "JFK";
        System.out.println(map);
        while(true){
            res.add(str);
            ArrayList<String> next_stops = map.getOrDefault(str, null);
            if(next_stops!=null && next_stops.size()!=0){
                do{
                    str = next_stops.get(0);
                    next_stops.remove(0);
                }while(!map.containsKey(str));
                
            } 
            else break;
        }
        return res;
    }
}