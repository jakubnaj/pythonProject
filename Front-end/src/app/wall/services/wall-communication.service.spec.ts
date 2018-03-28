import { TestBed, inject } from '@angular/core/testing';

import { WallCommunicationService } from './wall-communication.service';

describe('WallCommunicationService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [WallCommunicationService]
    });
  });

  it('should be created', inject([WallCommunicationService], (service: WallCommunicationService) => {
    expect(service).toBeTruthy();
  }));
});
