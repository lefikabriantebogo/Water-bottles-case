class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        # total bottles drunk
        total = numBottles

        empty = numBottles

        while empty >= numExchange:

            new_full = empty // numExchange
            total += new_full  # drink them
            # update empty count: remainder + newly emptied ones
            empty = empty % numExchange + new_full

        return total

