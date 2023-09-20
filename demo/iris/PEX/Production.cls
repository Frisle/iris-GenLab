Class PEX.Production Extends Ens.Production
{

XData ProductionDefinition
{
<Production Name="PEX.Production" TestingEnabled="true" LogGeneralTraceEvents="false">
  <Description></Description>
  <ActorPoolSize>2</ActorPoolSize>
  <Item Name="Python.FileOperation" Category="" ClassName="Python.FileOperation" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Adapter" Name="Charset">utf-8</Setting>
    <Setting Target="Adapter" Name="FilePath">/home/irisowner/dev/output/</Setting>
    <Setting Target="Host" Name="%settings">path=/home/irisowner/dev/output/</Setting>
  </Item>  
  <Item Name="Python.NERService" Category="" ClassName="Python.NERService" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
    <Setting Target="Host" Name="%settings">limit=10</Setting>
  </Item>  
  <Item Name="Python.FilterPostRoutingRule" Category="" ClassName="Python.FilterPostRoutingRule" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
  </Item>
</Production>
}

}
