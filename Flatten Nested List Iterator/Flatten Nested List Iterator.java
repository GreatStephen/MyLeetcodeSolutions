/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
import java.util.NoSuchElementException;
public class NestedIterator implements Iterator<Integer> {
    // 2 stacks solution
    // make sure that the first item in obj_stack.peek() is an integer, when hasNext()
    private Deque<Integer> index_stack;
    private Deque<List<NestedInteger>> obj_stack;

    public NestedIterator(List<NestedInteger> nestedList) {
        index_stack = new LinkedList();
        obj_stack = new LinkedList();
        index_stack.offerLast(0);
        obj_stack.offerLast(nestedList);
    }

    @Override
    public Integer next() {
        if(!hasNext()){
            throw new NoSuchElementException();
        }
        int index = index_stack.pollLast();
        index_stack.offerLast(index+1);
        return obj_stack.peekLast().get(index).getInteger();
    }

    @Override
    public boolean hasNext() {
        while(!obj_stack.isEmpty()){
            int index = index_stack.peekLast();
            List<NestedInteger> obj = obj_stack.peekLast();

            // end of current list
            if(index>=obj.size()){
                index_stack.pollLast();
                obj_stack.pollLast();
                continue;
            }

            // top element is an integer?
            if(obj.get(index).isInteger()){
                break;
            }
            else{
                index_stack.offerLast(index_stack.pollLast()+1);
                index_stack.offerLast(0);
                obj_stack.offerLast(obj.get(index).getList());
            }
        }

        return !index_stack.isEmpty();
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */