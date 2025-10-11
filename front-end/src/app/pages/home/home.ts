import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { NgxEchartsDirective, provideEchartsCore } from 'ngx-echarts';
import * as echarts from 'echarts/core';
import { BarChart, LineChart } from 'echarts/charts';
import { GridComponent, LegendComponent, TooltipComponent } from 'echarts/components';
import { CanvasRenderer } from 'echarts/renderers';
echarts.use([BarChart, LineChart, GridComponent, TooltipComponent, LegendComponent, CanvasRenderer]);

import { EChartsOption } from 'echarts/types/dist/shared';
import { EChartsCoreOption } from 'echarts/core';

@Component({
  selector: 'app-home',
  imports: [CommonModule, NgxEchartsDirective],
  templateUrl: './home.html',
  styleUrl: './home.css',
  providers: [provideEchartsCore({ echarts })],
})
export class Home {
  chartOption: EChartsOption = {
    grid: {
    top: 35,
    left: 40,
    right: 35,
    bottom: 35,
    containLabel: true
  },
  xAxis: {
    type: 'category',
    data: ['Jan', 'Fev', 'Mar', 'Abril', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    axisLabel: {
      color: '#fff',
      rotate: 45,
      interval: 0
    }
  },
  yAxis: {
    type: 'value',
    axisLabel:{
      color: '#fff',
    }
  },
  series: [
    {
      name: 'Vendas (mil)',
      type: 'line',
      data: [30, 20, 78, 50, 90, 120, 80, 60, 70, 100, 130, 150],
      color: '#fff',  
    }
  ]}
  chartOption2: EChartsCoreOption  =  { 
    xAxis : { 
      type: 'category', 
      data : [ 'Seg' ,  'Ter' ,  'Qua' ,  'Qui' ,  'Sex' ,  'Sáb' ,  'Dom' ] ,
      axisLabel:{
        color: '#fff',
      }
      
    } , 
    yAxis : { 
      type : 'value' ,
      axisLabel:{
        color: '#fff',
      }
      
    } , 
    series : [ 
      { 
        data : [ 820 ,  932 ,  901 ,  934 ,  1290 ,  1330 ,  1320 ] , 
        type : 'bar' , 
        color: '#fff', 
      } , 
    ] , 
  } ;
  chartOption3: EChartsCoreOption  =  { 
    xAxis : { 
      type: 'value', 
      axisLabel:{
        color: '#fff',
      }
      
    } , 
    yAxis : { 
      type : 'category' ,
      data : [ 'Seg' ,  'Ter' ,  'Qua' ,  'Qui' ,  'Sex'] ,
      axisLabel:{
        color: '#fff',
      }
      
    } , 
    series : [ 
      { 
        name: 'Vendas (mi)',
        data : [ 820 ,  932 ,  901 ,  934 ,  1290 ,  1330 ,  1320 ] , 
        type : 'bar' , 
        color: '#fff', 
        label: {
          show: true,
          position: 'right', // mostra o valor na ponta da barra
          color: '#fff'
        }
      } , 
    ] , 
  } ;
metricValue: any;
}
