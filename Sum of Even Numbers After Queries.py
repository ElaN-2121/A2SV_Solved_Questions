       sum_even=sum([x for x in nums if x%2==0])
        res=[]
        for value, index in queries:

            if nums[index]%2==0:
                sum_even-=nums[index]

            nums[index]+=value
            if nums[index]%2==0:
                sum_even+=(nums[index])
                res.append(sum_even)
        return res
