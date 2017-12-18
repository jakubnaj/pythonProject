import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {RouterModule} from '@angular/router';

import {AppComponent} from './app.component';
import {NavigationModule} from './navigation/navigation.module';
import {WallModule} from './wall/wall.module';
import {RoutingModule} from './routing.module';
import {AccountModule} from './account/account.module'


@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    NavigationModule,
    WallModule,
    RoutingModule,
    RouterModule,
    AccountModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
