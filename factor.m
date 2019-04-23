load("net_adj_consumer.mat");
period=["2004-06-30" "2007-06-29";"2007-7-2" "2007-12-31";"2007-12-31" "2009-12-31";"2010-1-1" "2010-12-31";"2011-1-3" "2013-12-31";"2014-1-1" "2014-12-31";"2015-1-1" "2017-6-30";"2017-6-30" "2018-6-29"];

result={};
for j = 1 : 19
    res=[];
    data=net_adj{1,j};
    for i = 1 : size(period,1)
       
       t1=datenum(period(i,1));
       t2=datenum(period(i,2));
       
       if(data(1,1)>t2)
           continue;
       end
       if(data(1,1)>t1&&data(1,1)<t2)
           t1=data(1,1);
       end
       
       id1=[];
       id2=[];
       while(isempty(id1))
          [id1,~]=find(data==t1);
          t1=t1+1;
       end
       while(isempty(id2))
           [id2,~]=find(data==t2);
           t2=t2+1;
       end
       
       res=[res;period(i,1),data(id2,2)-data(id1,2)]; 
    end
    result{j}=res;
end
    