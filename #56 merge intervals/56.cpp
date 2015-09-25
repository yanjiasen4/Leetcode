/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
 
bool lcmp(Interval a, Interval b)
{
	return a.start < b.start;
}
 
class Solution {
public:
    vector<Interval> merge(vector<Interval>& intervals) {
        sort(intervals.begin(), intervals.end(), &lcmp);
		vector<Interval> result;
		if(intervals.empty())
		{
		    return result;
		}
		int size = intervals.size();
		for (int i = 0; i < size - 1; i++)
		{
			if (intervals[i].end >= intervals[i+1].start)
			{
			    intervals[i+1].start = intervals[i].start;
			    if(intervals[i].end > intervals[i+1].end)
			    {
				    intervals[i + 1].end = intervals[i].end;
			    }
			}
			else {
				result.push_back(intervals[i]);
			}
		}
		result.push_back(intervals[size - 1]);
		return result;
    }
};