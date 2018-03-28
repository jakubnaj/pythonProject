import { Injectable } from '@angular/core';
import { Subject } from 'rxjs/Subject';

@Injectable()
export class WallCommunicationService {
  activeName: Subject<string> = new Subject();
  constructor() {}

}
