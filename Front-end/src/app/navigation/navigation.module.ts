import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {HeaderHomeComponent} from './components/header-home/header-home.component';
import {RouterModule} from '@angular/router';
import { NavigationService } from './services/navigation.service';

@NgModule({
  imports: [
    CommonModule,
    RouterModule
  ],
  declarations: [HeaderHomeComponent],
  providers: [NavigationService],
  exports: [HeaderHomeComponent]
})
export class NavigationModule {
}
