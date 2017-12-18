import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {HeaderHomeComponent} from './components/header-home/header-home.component';
import {RouterModule} from '@angular/router';

@NgModule({
  imports: [
    CommonModule,
    RouterModule
  ],
  declarations: [HeaderHomeComponent],
  exports: [HeaderHomeComponent]
})
export class NavigationModule {
}
